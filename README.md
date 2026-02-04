# Toki Suno

Toki Suno is a light-based realisation of Toki Pona: a way to express Toki Pona concepts through colour and visual change rather than speech or humanoid gesture. It was created for a science-fiction setting, but is documented here as a standalone language design experiment.

The project grew from a broader question about communication across species. Experiments with animals using sound buttons show that, given simple symbols and repetition, intent and preference can emerge without shared language. At the same time, research into forests reveals non-verbal communication networks where meaning is distributed, environmental, and collective. These ideas suggest a possibility: that a minimal, non-human-centred communication system could support more complex and meaningful cross-species interaction.

Toki Suno explores what happens when language is constrained to a medium shared by all living systems: light. Colour carries lexical meaning, while structure is conveyed visually and over time, rather than through word order or grammatical markers. The result is a minimal, context-driven system designed for non-humanoid intelligences capable of perceiving and manipulating visual contrast.

---

## What It Is

Toki Suno keeps Toki Pona’s minimal vocabulary and context-driven meaning, and explores what happens when expression is constrained to light: colour carries lexical meaning, and structure is conveyed visually and temporally rather than through spoken particles or word order.

---

## Design Goals and Constraints

- Extremely small vocabulary (this implementation is smaller than Toki Pona)
- Minimal social assumptions (e.g. no money terms; no grammatical gender)
- Meaning remains context-driven; differing perspectives can lead to multiple valid interpretations
- Designed for non-humanoid intelligences that can manipulate colour and visual contrast
- Expression is sensitive to environmental conditions; ambient light and contrast can limit or alter perception

---

## Repository Contents

- `grammar.md` — how utterances are structured (rendering, boundaries, attachment, visual roles)
- `lexicon.md` — colour mappings for words
- `examples.md` — short samples

---

## Credit

Inspired by Toki Pona (Sonja Lang). The structure was also informed by signed interpretations of toki pona.

---

## Feedback

If you spot inconsistencies or edge cases, open an issue with:
- the intended Toki Pona gloss
- what you expected the structure to be
- why the current rules don’t cover it
