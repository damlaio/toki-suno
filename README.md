# Toki Suno

Toki Suno is a light-based realisation of Toki Pona: a way to express Toki Pona concepts through colour and visual change rather than speech or humanoid gesture. It was created for a science-fiction setting, but is documented here as a standalone language design experiment.

The project grew from a broader question about communication across species. Experiments with animals using sound buttons show that, given simple symbols and repetition, intent and preference can emerge without shared language. At the same time, research into forests reveals non-verbal communication networks where meaning is distributed, environmental, and collective. These ideas suggest a possibility: that a minimal, non-human-centred communication system could support more complex and meaningful cross-species interaction.

Toki Suno explores what happens when language is constrained to a medium shared by all living systems: light. Colour carries lexical meaning, while structure is conveyed visually and over time, rather than through word order or grammatical markers. The result is a minimal, context-driven system designed for non-humanoid intelligences capable of perceiving and manipulating visual contrast.

---

## What it is

Toki Suno keeps Toki Pona’s minimal vocabulary and context-driven meaning, and explores what happens when expression is constrained to light: colour carries lexical meaning, and structure is conveyed visually and temporally rather than through spoken particles or word order.

---

## Design goals and constraints

- Extremely small vocabulary (this implementation is smaller than Toki Pona)
- Minimal social assumptions (e.g. no money terms; no grammatical gender)
- Meaning remains context-driven; differing perspectives can lead to multiple valid interpretations
- Designed for non-humanoid intelligences that can manipulate colour and visual contrast
- Expression is sensitive to environmental conditions; ambient light and contrast can limit or alter perception

---

## Repository contents

### Structure
- `grammar.md` — how utterances are structured (boundaries, attachment, visual roles)

### Vocabulary
- `lexicon.md` — colour mappings for words

### Examples
- `examples.md` — short illustrative samples  
- `rendering.md` — documentation display notes for the examples


---

## Quick examples (with colour)

<style>
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
  border: 2px solid #fff !important;
}

.frame-v {
  border: 2px solid rgba(255,255,255,0.35) !important;
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
  border: 2px solid #fff !important;
  animation: frame-pulse 1s ease-in-out infinite;
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
  margin: 4px 0;
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
</style>

### Easy

**toki pona:** `toki`  
**gloss:** hello  
**colour rendering:** `(Purple)`  
**display:**<br> <span class="seq-display seq-enabled" style="--seq-group-count:1;"><span class="seq-group" style="--seq-i:0;"><span style="display:inline-block;width:36px;height:12px;background:#7E57C2;border:1px solid #888;"></span></span></span>

### Medium

**toki pona:** `soweli kon kule loje`  
**gloss:** red bird  
**colour rendering:** `(Green + Light Blue + Pink) (Dark Blue) (Brown + Light Blue + Dark Blue) (Red)`  
**display:**<br>
<span class="seq-display seq-enabled" style="--seq-group-count:1;"><span class="seq-group" style="--seq-i:0;"><span style="display:inline-block;width:12px;height:12px;background:#2E8B57;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#FF6FAE;border:1px solid #888;"></span>  <span style="display:inline-block;width:36px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>  <span style="display:inline-block;width:12px;height:12px;background:#8B5A2B;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>  <span style="display:inline-block;width:36px;height:12px;background:#E53935;border:1px solid #888;"></span></span></span>

### Hard

**toki pona:** `tenpo lape la jan li moku ala`  
**gloss:** when sleeping, the person does not eat  
**colour rendering:** `(Purple + Yellow + Dark Blue) (Light Blue + Dark Blue) (Purple + Dark Blue + Brown) | {S Red + Light Blue + Yellow} | {V Dark Blue + Red} (dotted white frame)`  
**display:**<br>
<span class="seq-display seq-enabled" style="--seq-group-count:3;"><span class="seq-group" style="--seq-i:0;"><span style="display:inline-block;width:12px;height:12px;background:#7E57C2;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#F4D03F;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>  <span style="display:inline-block;width:18px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>  <span style="display:inline-block;width:12px;height:12px;background:#7E57C2;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#8B5A2B;border:1px solid #888;"></span></span><span class="seq-group" style="--seq-i:1;"><span class="frame frame-s" style="display:inline-flex;align-items:center;padding:2px;border:2px solid #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:12px;height:12px;background:#E53935;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#F4D03F;border:1px solid #888;"></span></span></span><span class="seq-group" style="--seq-i:2;"><span class="frame frame-v" style="display:inline-flex;align-items:center;padding:2px;border:2px dashed #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:18px;height:12px;background:#E53935;border:1px solid #888;"></span></span>  <span style="display:inline-block;width:36px;height:12px;box-sizing:border-box;background:transparent;border:2px dotted #FFFFFF;"></span></span></span>

The renderings above are illustrative only. Animated role frames and sequential reveal are optional enhancements: Markdown provides static fallback frames, while custom HTML renderers may apply the CSS specification defined in `rendering.md` for flowing/pulsating effects and pause-driven reveal.

For a guaranteed live animation preview, open `examples.html`.

Canonical rendering specification: `rendering.md`.


---

## Credit

Inspired by Toki Pona (Sonja Lang). The structure was also informed by signed interpretations of toki pona.

---

## Feedback

If you spot inconsistencies or edge cases, open an issue with:
- the intended Toki Pona gloss
- what you expected the structure to be
- why the current rules don’t cover it

