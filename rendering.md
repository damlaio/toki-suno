# Toki Suno Rendering Contract

## Scope

This document defines how example displays are represented in project documentation and preview surfaces.
It covers frame classes, fallback behavior, CSS enhancement, and accessibility constraints.
It is not part of the conlang grammar itself.

## Role Frame Model

Role heads use a shared wrapper pattern:

- Subject: `<span class="frame frame-s">...</span>`
- Verb: `<span class="frame frame-v">...</span>`
- Object: `<span class="frame frame-o">...</span>`
- Lexical color blocks inside frames may use `<span class="token">...</span>`

## Markdown Fallback Rules

In Markdown-first environments (including GitHub), keep inline fallback styles on each frame:

- `.frame.frame-s`: solid white border
- `.frame.frame-v`: dashed white border (static fallback for flowing)
- `.frame.frame-o`: dotted white border (static fallback for pulsating)
- all frames: rounded rectangle, small padding, `inline-flex` layout

## CSS Enhancement Contract

Canonical CSS source of truth:

```css
.frame {
  position: relative;
  display: inline-flex;
  align-items: center;
  padding: 2px;
  border-radius: 6px;
  box-sizing: border-box;
  vertical-align: middle;
}

.frame-s {
  border: 2px solid #fff;
}

.frame-v {
  border: 2px solid #fff;
  background-image: linear-gradient(110deg, transparent 0%, rgba(255,255,255,0.45) 48%, transparent 74%);
  background-size: 260% 100%;
  animation: frame-flow 1.35s linear infinite;
  box-shadow: 0 0 0 1px rgba(255,255,255,0.35), 0 0 8px rgba(255,255,255,0.28);
}

.frame-o {
  border: 2px solid #fff;
  animation: frame-pulse 1s ease-in-out infinite;
}

@keyframes frame-flow {
  0% {
    background-position: 180% 0;
    box-shadow: 0 0 0 1px rgba(255,255,255,0.3), 0 0 6px rgba(255,255,255,0.24);
  }
  50% {
    box-shadow: 0 0 0 1px rgba(255,255,255,0.5), 0 0 12px rgba(255,255,255,0.4);
  }
  100% {
    background-position: -80% 0;
    box-shadow: 0 0 0 1px rgba(255,255,255,0.3), 0 0 6px rgba(255,255,255,0.24);
  }
}

@keyframes frame-pulse {
  0%, 100% {
    transform: scale(1);
    box-shadow: 0 0 0 0 rgba(255,255,255,0.12), 0 0 4px rgba(255,255,255,0.2);
  }
  50% {
    transform: scale(1.03);
    box-shadow: 0 0 0 3px rgba(255,255,255,0.58), 0 0 13px rgba(255,255,255,0.48);
  }
}
```

## Accessibility (prefers-reduced-motion)

When reduced motion is requested, animated role frames must stop motion:

```css
@media (prefers-reduced-motion: reduce) {
  .frame-v, .frame-o {
    animation: none;
    background-image: none;
  }
}
```

## Reference Implementations

- `examples.md`: Markdown-facing examples with embedded enhancement CSS.
- `examples.html`: guaranteed runnable animated preview surface.
- `README.md`: quick examples and project-facing rendering snippets.

Content deduplication policy:

- Canonical CSS lives in `rendering.md`.
- Applied CSS in other docs is an implementation copy.
- Update `rendering.md` first, then sync copied blocks.
