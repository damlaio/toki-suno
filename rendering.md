# Rendering Specification for Documentation Examples

## Scope

This document defines how Toki Suno examples are displayed in project documentation and preview environments. It specifies frame classes, Markdown fallback behaviour, CSS enhancements, and accessibility requirements. It does not define any part of the conlang grammar.

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
  border: 2px solid rgba(255,255,255,0.35);
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 0 1px rgba(255,255,255,0.25), 0 0 6px rgba(255,255,255,0.2);
}

.frame-v::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background:
    repeating-linear-gradient(
      90deg,
      rgba(255,255,255,0.92) 0 8px,
      rgba(255,255,255,0.18) 8px 16px
    ) top / 200% 2px no-repeat,
    repeating-linear-gradient(
      0deg,
      rgba(255,255,255,0.92) 0 8px,
      rgba(255,255,255,0.18) 8px 16px
    ) right / 2px 200% no-repeat,
    repeating-linear-gradient(
      90deg,
      rgba(255,255,255,0.92) 0 8px,
      rgba(255,255,255,0.18) 8px 16px
    ) bottom / 200% 2px no-repeat,
    repeating-linear-gradient(
      0deg,
      rgba(255,255,255,0.92) 0 8px,
      rgba(255,255,255,0.18) 8px 16px
    ) left / 2px 200% no-repeat;
  animation: frame-flow 0.9s linear infinite;
  pointer-events: none;
}

.frame-o {
  border: 2px solid #fff;
  animation: frame-pulse 1s ease-in-out infinite;
}

@keyframes frame-flow {
  from {
    background-position: 0 0, 100% 0, 0 100%, 0 0;
  }
  to {
    background-position: 16px 0, 100% 16px, -16px 100%, 0 -16px;
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

.seq-display {
  position: relative;
  display: inline-block;
  --seq-group-count: 1;
  --seq-show: 2s;
  --seq-pause: 0.5s;
  --seq-step: calc(var(--seq-show) + var(--seq-pause));
  --seq-total: calc(var(--seq-group-count) * var(--seq-step));
}

.seq-group {
  display: block;
}

.seq-enabled .seq-group {
  opacity: 1;
}

.seq-enabled:is(:hover, :focus-within) .seq-group {
  opacity: 0;
  animation-name: seq-group-final, seq-group-stage;
  animation-duration: var(--seq-total), var(--seq-step);
  animation-timing-function: linear, linear;
  animation-iteration-count: 1, 1;
  animation-fill-mode: forwards, none;
  animation-delay: 0s, calc(var(--seq-i) * var(--seq-step));
}

.seq-enabled::before {
  content: "";
  position: absolute;
  inset: 0;
  background: #000;
  pointer-events: none;
  z-index: 3;
  opacity: 0;
}

.seq-enabled:is(:hover, :focus-within)::before {
  animation-name: seq-blockout-cycle;
  animation-duration: var(--seq-step);
  animation-timing-function: linear;
  animation-iteration-count: var(--seq-group-count);
}

@keyframes seq-group-final {
  0% {
    opacity: 0;
  }
  99.99% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes seq-group-stage {
  0% {
    opacity: 1;
  }
  80% {
    opacity: 1;
  }
  80.0001% {
    opacity: 0;
  }
  100% {
    opacity: 0;
  }
}

@keyframes seq-blockout-cycle {
  0% {
    opacity: 0;
  }
  80% {
    opacity: 0;
  }
  80.0001% {
    opacity: 1;
  }
  100% {
    opacity: 1;
  }
}

```

Sequential reveal is additive to role frame effects: `.frame-v` flow and `.frame-o` pulse remain active while groups are revealed.

## Accessibility (prefers-reduced-motion)

When reduced motion is requested, animated role frames must stop motion:

```css
@media (prefers-reduced-motion: reduce) {
  .frame-v, .frame-o {
    animation: none;
    background-image: none;
  }
  .frame-v::after {
    animation: none;
  }
  .seq-enabled::before {
    animation: none;
    opacity: 0;
  }
  .seq-enabled .seq-group {
    animation: none;
    opacity: 1;
  }
}
```

## Sequential Reveal Contract (CSS-only, no JS)

Use this contract for pause-driven reveal without JavaScript:

- Container: `<span class="seq-display seq-enabled">...</span>`
- Group item: `<span class="seq-group" style="--seq-i:N;">...</span>`
- Optional marker for final state handling: `.seq-final`

Required container variables:

- `--seq-group-count`: total number of groups
- `--seq-show`: visible segment duration (locked default `2s`)
- `--seq-pause`: pause blockout duration (locked default `0.5s`)
- `--seq-step`: `calc(var(--seq-show) + var(--seq-pause))`
- `--seq-total`: `calc(var(--seq-group-count) * var(--seq-step))`

Timeline semantics:

- Sequence starts on hover/focus of the sentence viewport.
- Group 1 appears first.
- Pause segments are full blackout.
- During sequence, only the current group is visible.
- After the last group cycle, full sentence appears.
- While hovered/focused, final full-sentence state remains visible.
- When hover/focus ends, the static full sentence state is shown.

## Reference Implementations

- `examples.md`: Markdown-facing examples with embedded enhancement CSS.
- `examples.html`: guaranteed runnable animated preview surface.
- `README.md`: quick examples and project-facing rendering snippets.

Content deduplication policy:

- Canonical CSS lives in `rendering.md`.
- Applied CSS in other docs is an implementation copy.
- Update `rendering.md` first, then sync copied blocks.
