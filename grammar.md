# Toki Suno Grammar

Toki Suno is a light-based realisation inspired by Toki Pona.  
Grammar is expressed through **rendering order, pauses, framing, and colour**, rather than through particles or spatial word order.

This document describes how utterances are structured and interpreted in Toki Suno.

---

## 1. Core principle

An utterance in Toki Suno is revealed over time, but interpreted as a whole.

- Colour carries lexical meaning.
- White framing carries grammatical function.
- Pauses (darkness) mark boundaries.
- Rendering order determines structure and attachment.

There are no explicit grammatical particles.  
Special lexical renderings (used by some words) are separate from role frames and do not mark subject/verb/object. They take grammatical frames externally according to their role in the sentence.

---

## 2. Rendering order and pauses

Rendering order is essential to interpretation.

- Elements are illuminated in sequence for clarity.
- Within a group, previously revealed elements remain alight while modifiers are added.
- A pause (darkness) indicates the completion of a group.
- After a pause, attachment resets and a new group begins.

Pauses fulfil the structural role of particles such as *li* and *e*.

---

## 3. Heads and modifiers

Each group has a **head**, followed by **modifiers**.

- The head is framed in white and remains illuminated.
- Modifiers are shown in solid colour without a frame.
- Modifiers are revealed one by one in order.
- When needed, modifiers may be highlighted **simultaneously as a group**.

Modifier grouping is handled visually; no grouping word (such as *pi*) is used.

---

## 4. Subject group

- The subject head is shown in solid colour(s), framed by a **solid white frame**.
- Subject modifiers are revealed in solid colour(s) without a frame.
- Once the subject group is complete, a pause follows.
- For multiple subjects, the same procedure is repeated before moving on.

---

## 5. Verb group

- The verb head is shown in solid colour(s), framed by a **flowing white frame**.
- Verb modifiers are revealed in solid colour(s) without a frame.
- A pause follows once the verb group is complete.

---

## 6. Object group

- The object head is shown in solid colour(s), framed by a **pulsating white frame**.
- Object modifiers are revealed in solid colour(s) without a frame.
- Modifiers may be grouped visually when necessary.
- A pause closes the object group.

For multiple objects, the same procedure is repeated.

---

## 7. Preposition and connective words

Words such as **la**, **anu**, and **o** are treated as lexical items.

- Their function is determined by placement and rendering order.
- Attachment follows temporal proximity: a connective applies to what immediately follows, unless a pause intervenes.

---

## 8. Attachment rules

Attachment is determined by rendering order.

- A modifier or group attaches to the most recently completed head.
- A pause closes the current attachment scope.
- Grouped highlighting overrides simple proximity when used.

This replaces syntactic markers used in spoken languages.

---

## 9. Negation and questions

Toki Suno does not introduce special grammatical mechanisms for negation or questions.

- Negation is expressed lexically using **ala**, following Toki Pona usage.
- Questions are expressed lexically using **seme**.

Their visual rendering is defined in the lexicon.

---

## 10. Flexibility

The grammar of Toki Suno is not prescriptive.

The system is designed to:
- adapt to different visual implementations
- tolerate variation
- evolve as new constraints are explored

---

## 11. Display frame implementation

For documentation displays, role heads use a shared wrapper pattern:
The contract is implemented directly in `examples.md` (best effort in Markdown renderers) and fully runnable in `examples.html`.

- Subject: `<span class="frame frame-s">...</span>`
- Verb: `<span class="frame frame-v">...</span>`
- Object: `<span class="frame frame-o">...</span>`
- Lexical colour blocks inside frames may use `<span class="token">...</span>`

### Static Markdown fallback

In Markdown-first environments (including GitHub), keep inline fallback styles on each frame:

- `.frame.frame-s`: solid white border
- `.frame.frame-v`: dashed white border (static fallback for flowing)
- `.frame.frame-o`: dotted white border (static fallback for pulsating)
- all frames: rounded rectangle, small padding, `inline-flex` layout

### CSS enhancement contract (for custom HTML renderers)

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

@media (prefers-reduced-motion: reduce) {
  .frame-v, .frame-o {
    animation: none;
    background-image: none;
  }
}
```
