#!/usr/bin/env python3
"""Build static HTML pages in the local pages/ folder from root Markdown sources."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import pathlib
import re
import shutil
from typing import Dict, Iterable, List, Tuple
from urllib.parse import urlsplit, urlunsplit

import markdown
from markdown.extensions.toc import TocExtension

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / "pages"
SITE_DIR = ROOT / "site"

DOCS: List[Dict[str, str]] = [
    {"source": "README.md", "output": "index.html", "title": "Home"},
    {"source": "grammar.md", "output": "grammar.html", "title": "Grammar"},
    {"source": "lexicon.md", "output": "lexicon.html", "title": "Lexicon"},
    {"source": "examples.md", "output": "examples.html", "title": "Examples"},
    {"source": "rendering.md", "output": "rendering.html", "title": "Rendering"},
]


def github_slugify(value: str, separator: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"[\s_-]+", separator, value)
    value = re.sub(rf"{re.escape(separator)}+", separator, value)
    value = value.strip(separator)
    return value or "section"


def build_markdown_converter() -> markdown.Markdown:
    return markdown.Markdown(
        extensions=[
            "extra",
            "sane_lists",
            "md_in_html",
            TocExtension(permalink=False, slugify=github_slugify),
        ],
        output_format="html5",
    )


def normalize_local_path(path_value: str) -> str:
    normalized = path_value.replace("\\", "/")
    if normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def rewrite_md_links(html_text: str, link_map: Dict[str, str]) -> str:
    href_re = re.compile(r'href=(["\'])([^"\']+)\1', re.IGNORECASE)

    def replace(match: re.Match[str]) -> str:
        quote = match.group(1)
        href = match.group(2)
        parsed = urlsplit(href)

        if parsed.scheme or href.startswith("//"):
            return match.group(0)
        if href.startswith("#"):
            return match.group(0)

        path_part = normalize_local_path(parsed.path)
        mapped = link_map.get(path_part)
        if mapped is None and path_part.endswith(".md"):
            mapped = link_map.get(pathlib.Path(path_part).name)
        if mapped is None:
            return match.group(0)

        rebuilt = urlunsplit((parsed.scheme, parsed.netloc, mapped, parsed.query, parsed.fragment))
        return f"href={quote}{rebuilt}{quote}"

    return href_re.sub(replace, html_text)


def render_nav(current_output: str) -> str:
    items = []
    for doc in DOCS:
        is_active = " class=\"active\"" if doc["output"] == current_output else ""
        items.append(f'<a href="{doc["output"]}"{is_active}>{html.escape(doc["title"])}</a>')
    return "\n".join(items)


def iter_tokens(tokens: Iterable[dict], max_level: int = 3) -> Iterable[Tuple[int, str, str]]:
    for token in tokens:
        level = int(token.get("level", 0))
        if level <= max_level:
            yield level, token.get("id", ""), token.get("name", "")
        children = token.get("children", [])
        if children:
            yield from iter_tokens(children, max_level=max_level)


def build_index_hub(doc_tokens: Dict[str, List[dict]]) -> str:
    page_links = "\n".join(
        f'<li><a href="{doc["output"]}">{html.escape(doc["title"])}</a></li>' for doc in DOCS
    )

    section_blocks: List[str] = []
    for doc in DOCS:
        tokens = doc_tokens[doc["source"]]
        section_items = []
        for level, token_id, name in iter_tokens(tokens, max_level=3):
            if level < 2 or not token_id:
                continue
            label = html.escape(name)
            section_items.append(f'<li><a href="{doc["output"]}#{token_id}">{label}</a></li>')
        if not section_items:
            continue
        summary = html.escape(doc["title"])
        section_blocks.append(
            "<details open>"
            f'<summary><a href="{doc["output"]}">{summary}</a></summary>'
            f"<ul>{''.join(section_items)}</ul>"
            "</details>"
        )

    return (
        '<section class="docs-hub">'
        "<h2>Site Map</h2>"
        "<p>This index links every generated page plus major section anchors.</p>"
        f"<ul>{page_links}</ul>"
        "<h3>Section TOC</h3>"
        f"{''.join(section_blocks)}"
        "</section>"
    )


def fill_template(template: str, *, page_title: str, nav_html: str, content_html: str, source_name: str) -> str:
    generated_at = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return (
        template.replace("{{PAGE_TITLE}}", html.escape(page_title))
        .replace("{{NAV_LINKS}}", nav_html)
        .replace("{{CONTENT}}", content_html)
        .replace("{{SOURCE_FILE}}", html.escape(source_name))
        .replace("{{GENERATED_AT}}", generated_at)
    )


def find_local_links(page_html: str) -> List[str]:
    href_re = re.compile(r'href=(["\'])([^"\']+)\1', re.IGNORECASE)
    links: List[str] = []
    for match in href_re.finditer(page_html):
        href = match.group(2)
        parsed = urlsplit(href)
        if parsed.scheme or href.startswith("//"):
            continue
        if href.startswith("mailto:"):
            continue
        links.append(href)
    return links


def validate_local_links(output_pages: Dict[str, str]) -> None:
    anchors_by_page: Dict[str, set[str]] = {}
    for page_name, page_html in output_pages.items():
        anchors = set()
        for _, anchor in re.findall(r'id=(["\'])([^"\']+)\1', page_html, re.IGNORECASE):
            anchors.add(anchor)
        anchors_by_page[page_name] = anchors

    errors: List[str] = []
    for page_name, page_html in output_pages.items():
        for href in find_local_links(page_html):
            parsed = urlsplit(href)
            target_page = parsed.path or page_name
            if target_page.startswith("/"):
                target_page = target_page[1:]
            ext = pathlib.Path(target_page).suffix.lower()
            if ext and ext != ".html":
                # Ignore local asset links (e.g. site.css, images).
                continue

            if target_page not in output_pages:
                errors.append(f"{page_name}: missing target page '{href}'")
                continue

            if parsed.fragment and parsed.fragment not in anchors_by_page[target_page]:
                errors.append(f"{page_name}: missing anchor '{parsed.fragment}' in '{target_page}'")

    if errors:
        message = "\n".join(f"- {entry}" for entry in errors)
        raise RuntimeError(f"Link validation failed:\n{message}")


def build_pages(check_links: bool) -> None:
    template = (SITE_DIR / "template.html").read_text(encoding="utf-8")
    style_src = SITE_DIR / "site.css"
    pages_style_dst = PAGES_DIR / "site.css"

    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(style_src, pages_style_dst)
    (PAGES_DIR / ".nojekyll").write_text("\n", encoding="utf-8")

    link_map = {doc["source"]: doc["output"] for doc in DOCS}
    rendered_content: Dict[str, str] = {}
    toc_tokens_by_source: Dict[str, List[dict]] = {}

    for doc in DOCS:
        source_path = ROOT / doc["source"]
        text = source_path.read_text(encoding="utf-8")
        md = build_markdown_converter()
        raw_content = md.convert(text)
        html_content = rewrite_md_links(raw_content, link_map)
        rendered_content[doc["source"]] = html_content
        toc_tokens_by_source[doc["source"]] = getattr(md, "toc_tokens", [])

    index_hub = build_index_hub(toc_tokens_by_source)
    output_pages: Dict[str, str] = {}

    for doc in DOCS:
        source_name = doc["source"]
        content = rendered_content[source_name]
        if source_name == "README.md":
            content = index_hub + content
        page_html = fill_template(
            template,
            page_title=doc["title"],
            nav_html=render_nav(doc["output"]),
            content_html=content,
            source_name=source_name,
        )
        output_pages[doc["output"]] = page_html
        (PAGES_DIR / doc["output"]).write_text(page_html, encoding="utf-8")

    if check_links:
        validate_local_links(output_pages)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build local pages HTML from Markdown docs.")
    parser.add_argument(
        "--skip-link-check",
        action="store_true",
        help="Skip local link and anchor validation.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_pages(check_links=not args.skip_link_check)


if __name__ == "__main__":
    main()
