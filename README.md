# toki suno

toki suno is a light-based realisation of toki pona: a way to communicate toki pona concepts through colour and visual change rather than speech or humanoid gesture.

It was created for a science-fiction setting, but is documented here as a standalone language design experiment.

---

## what it is (in one paragraph)

toki suno keeps toki pona’s minimal vocabulary and context-driven meaning, and explores what happens when expression is constrained to light: colour carries lexical meaning, and structure is conveyed visually and temporally rather than through spoken particles or word order.

---

## design goals and constraints

- extremely small vocabulary (this implementation is smaller than toki pona)
- minimal social assumptions (e.g. no money terms; no grammatical gender)
- meaning remains context-driven; differing perspectives can lead to multiple valid interpretations
- designed for non-humanoid intelligences that can manipulate colour and visual contrast

---

## repository contents

- `grammar.md` — how utterances are structured (rendering, boundaries, attachment, visual roles)
- lexicon — colour mappings for words (currently being migrated into a plain `lexicon.md`)
- examples — short samples

---

## credit

inspired by toki pona (Sonja Lang). the structure was also informed by signed interpretations of toki pona.

---

## feedback

If you spot inconsistencies or edge cases, open an issue with:
- the intended toki pona gloss
- what you expected the structure to be
- why the current rules don’t cover it
