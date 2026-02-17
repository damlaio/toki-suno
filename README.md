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

- `grammar.md` — how utterances are structured (rendering, boundaries, attachment, visual roles)
- `lexicon.md` — colour mappings for words
- `examples.md` — short samples

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
  border: 2px solid #fff !important;
  background-image: linear-gradient(110deg, transparent 0%, rgba(255,255,255,0.45) 48%, transparent 74%);
  background-size: 260% 100%;
  animation: frame-flow 1.35s linear infinite;
  box-shadow: 0 0 0 1px rgba(255,255,255,0.35), 0 0 8px rgba(255,255,255,0.28);
}

.frame-o {
  border: 2px solid #fff !important;
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

@media (prefers-reduced-motion: reduce) {
  .frame-v, .frame-o {
    animation: none;
    background-image: none;
  }
}
</style>

### Easy

**toki pona:** `toki`  
**gloss:** hello  
**colour rendering:** `(Purple)`  
**display:**<br> (<span style="display:inline-block;width:36px;height:12px;background:#7E57C2;border:1px solid #888;"></span>)

### Medium

**toki pona:** `soweli kon kule loje`  
**gloss:** red bird  
**colour rendering:** `(Green + Light Blue + Pink) (Dark Blue) (Brown + Light Blue + Dark Blue) (Red)`  
**display:**<br>
(<span style="display:inline-block;width:12px;height:12px;background:#2E8B57;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#FF6FAE;border:1px solid #888;"></span>)  (<span style="display:inline-block;width:36px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>)  (<span style="display:inline-block;width:12px;height:12px;background:#8B5A2B;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>)  (<span style="display:inline-block;width:36px;height:12px;background:#E53935;border:1px solid #888;"></span>)

### Hard

**toki pona:** `tenpo lape la jan li moku ala`  
**gloss:** when sleeping, the person does not eat  
**colour rendering:** `(Purple + Yellow + Dark Blue) (Light Blue + Dark Blue) (Purple + Dark Blue + Brown) | {S Red + Light Blue + Yellow} | {V Dark Blue + Red} (dotted white frame)`  
**display:**<br>
(<span style="display:inline-block;width:12px;height:12px;background:#7E57C2;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#F4D03F;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>)  (<span style="display:inline-block;width:18px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>)  (<span style="display:inline-block;width:12px;height:12px;background:#7E57C2;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#8B5A2B;border:1px solid #888;"></span>)<br>
<span class="frame frame-s" style="display:inline-flex;align-items:center;padding:2px;border:2px solid #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:12px;height:12px;background:#E53935;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#F4D03F;border:1px solid #888;"></span></span><br>
<span class="frame frame-v" style="display:inline-flex;align-items:center;padding:2px;border:2px dashed #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:18px;height:12px;background:#E53935;border:1px solid #888;"></span></span>  (<span style="display:inline-block;width:36px;height:12px;box-sizing:border-box;background:transparent;border:2px dotted #FFFFFF;"></span>)

Animated role frames are enhancement-only: Markdown keeps static fallback frames, while custom HTML renderers can apply the CSS contract in `grammar.md` for flowing/pulsating effects.
For guaranteed live animation preview, open `examples.html`.

---

## Credit

Inspired by Toki Pona (Sonja Lang). The structure was also informed by signed interpretations of toki pona.

---

## Feedback

If you spot inconsistencies or edge cases, open an issue with:
- the intended Toki Pona gloss
- what you expected the structure to be
- why the current rules don’t cover it
