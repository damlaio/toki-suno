# Examples

## Legend

{S … }  subject frame (`frame frame-s`; solid white frame in fallback)  
{V … }  verb frame (`frame frame-v`; flowing in CSS, dashed in fallback)  
{O … }  object frame (`frame frame-o`; pulsating in CSS, dotted in fallback)

( … )   lexical element or modifier (unframed)  
|       pause / darkness (group boundary; establishes clause structure)

---

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

## 1. Greeting

**toki pona:**  
`toki!`

*hello*

**structure:**  
`(toki)`

**colour rendering:**  
`(Purple)`

**display:**  
(<span style="display:inline-block;width:36px;height:12px;background:#7E57C2;border:1px solid #888;"></span>)

---

## 2. Noun phrase (bird without using waso)

**toki pona:**  
`soweli kon`

*bird (lit. air animal)*

**structure:**  
`(soweli) (kon)`  

**colour rendering:**  
`(Green + Light Blue + Pink) (Dark Blue)`

**display:**  
(<span style="display:inline-block;width:12px;height:12px;background:#2E8B57;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#FF6FAE;border:1px solid #888;"></span>)  (<span style="display:inline-block;width:36px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>)

---

## 3. Noun phrase with colour

**toki pona:**  
`soweli kon kule loje`

*red bird*

**structure:**  
`(soweli) (kon) (kule loje)`  

**colour rendering:**  
`(Green + Light Blue + Pink) (Dark Blue) (Brown + Light Blue + Dark Blue) (Red)`

**display:**  
(<span style="display:inline-block;width:12px;height:12px;background:#2E8B57;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#FF6FAE;border:1px solid #888;"></span>)  (<span style="display:inline-block;width:36px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>)  (<span style="display:inline-block;width:12px;height:12px;background:#8B5A2B;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>)  (<span style="display:inline-block;width:36px;height:12px;background:#E53935;border:1px solid #888;"></span>)

---

## 4. Intransitive predicate

**toki pona:**  
`soweli li moku`

*the animal eats*

**structure:**  
`{S soweli}`<br>
`|`<br>
`{V moku}`

**colour rendering:**  
`{S Green + Light Blue + Pink}`<br>
`|`<br>
`{V Dark Blue + Red}`

**display:**  
<span class="frame frame-s" style="display:inline-flex;align-items:center;padding:2px;border:2px solid #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:12px;height:12px;background:#2E8B57;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#FF6FAE;border:1px solid #888;"></span></span><br>
<span class="frame frame-v" style="display:inline-flex;align-items:center;padding:2px;border:2px dashed #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:18px;height:12px;background:#E53935;border:1px solid #888;"></span></span>

---

## 5. First person predicates with modifiers

**toki pona:**  
`mi moku pona`  

*I eat well / I eat good food*

**structure:**  
`{S mi}`<br>
`|`<br>
`{V moku} (pona)`

**colour rendering:**  
`{S Yellow + Light Blue}`<br>
`|`<br>
`{V Dark Blue + Red} (Pink)`

**display:**  
<span class="frame frame-s" style="display:inline-flex;align-items:center;padding:2px;border:2px solid #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:18px;height:12px;background:#F4D03F;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:18px;height:12px;background:#66CCFF;border:1px solid #888;"></span></span><br>
<span class="frame frame-v" style="display:inline-flex;align-items:center;padding:2px;border:2px dashed #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:18px;height:12px;background:#E53935;border:1px solid #888;"></span></span>  (<span style="display:inline-block;width:36px;height:12px;background:#FF6FAE;border:1px solid #888;"></span>)

---

**toki pona:**  
`mi pona moku`  

*I am good at eating*

**structure:**  
`{S mi}`<br>
`|`<br>
`{V pona} (moku)`

**colour rendering:**  
`{S Yellow + Light Blue}`<br>
`|`<br>
`{V Pink} (Dark Blue + Red)`

**display:**  
<span class="frame frame-s" style="display:inline-flex;align-items:center;padding:2px;border:2px solid #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:18px;height:12px;background:#F4D03F;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:18px;height:12px;background:#66CCFF;border:1px solid #888;"></span></span><br>
<span class="frame frame-v" style="display:inline-flex;align-items:center;padding:2px;border:2px dashed #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:36px;height:12px;background:#FF6FAE;border:1px solid #888;"></span></span>  (<span style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span style="display:inline-block;width:18px;height:12px;background:#E53935;border:1px solid #888;"></span>)

---

## 6. Transitive predicate

**toki pona:**  
`jan li moku e kili`

*the person eats fruit*

**structure:**  
`{S jan}`<br>
`|`<br>
`{V moku}`<br>
`|`<br>
`{O kili}`

**colour rendering:**  
`{S Red + Light Blue + Yellow}`<br>
`|`<br>
`{V Dark Blue + Red}`<br>
`|`<br>
`{O Pink + Green + Brown}`

**display:**  
<span class="frame frame-s" style="display:inline-flex;align-items:center;padding:2px;border:2px solid #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:12px;height:12px;background:#E53935;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#F4D03F;border:1px solid #888;"></span></span><br>
<span class="frame frame-v" style="display:inline-flex;align-items:center;padding:2px;border:2px dashed #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:18px;height:12px;background:#E53935;border:1px solid #888;"></span></span>
<br>
<span class="frame frame-o" style="display:inline-flex;align-items:center;padding:2px;border:2px dotted #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:12px;height:12px;background:#FF6FAE;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#2E8B57;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#8B5A2B;border:1px solid #888;"></span></span>

---

## 7. Predicate adjective

**toki pona:**  
`jan li pona`

*the person is good*

**structure:**  
`{S jan}`<br>
`|`<br>
`{V pona}`

**colour rendering:**  
`{S Red + Light Blue + Yellow}`<br>
`|`<br>
`{V Pink}`

**display:**  
<span class="frame frame-s" style="display:inline-flex;align-items:center;padding:2px;border:2px solid #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:12px;height:12px;background:#E53935;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#F4D03F;border:1px solid #888;"></span></span><br>
<span class="frame frame-v" style="display:inline-flex;align-items:center;padding:2px;border:2px dashed #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:36px;height:12px;background:#FF6FAE;border:1px solid #888;"></span></span>

---

## 8. Context setting

**toki pona:**  
`tenpo lape la jan li moku`

*when sleeping / after sleeping, the person eats*

**structure:**  
`(tenpo) (lape) (la)`<br>
`|`<br>
`{S jan}`<br>
`|`<br>
`{V moku}`

**colour rendering:**  
`(Purple + Yellow + Dark Blue) (Light Blue + Dark Blue) (Purple + Dark Blue + Brown)`<br>
`|`<br>
`{S Red + Light Blue + Yellow}`<br>
`|`<br>
`{V Dark Blue + Red}`

**display:**  
(<span style="display:inline-block;width:12px;height:12px;background:#7E57C2;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#F4D03F;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>)  (<span style="display:inline-block;width:18px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span>)  (<span style="display:inline-block;width:12px;height:12px;background:#7E57C2;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span style="display:inline-block;width:12px;height:12px;background:#8B5A2B;border:1px solid #888;"></span>)<br>
<span class="frame frame-s" style="display:inline-flex;align-items:center;padding:2px;border:2px solid #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:12px;height:12px;background:#E53935;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#F4D03F;border:1px solid #888;"></span></span>
<br>
<span class="frame frame-v" style="display:inline-flex;align-items:center;padding:2px;border:2px dashed #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:18px;height:12px;background:#E53935;border:1px solid #888;"></span></span>

---

## 9. Negation

**toki pona:**  
`jan li moku ala`

*the person does not eat*

**structure:**  
`{S jan}`<br>
`|`<br>
`{V moku} (ala)`

**colour rendering:**  
`{S Red + Light Blue + Yellow}`<br>
`|`<br>
`{V Dark Blue + Red} (dotted white frame)`

**display:**  
<span class="frame frame-s" style="display:inline-flex;align-items:center;padding:2px;border:2px solid #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:12px;height:12px;background:#E53935;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#F4D03F;border:1px solid #888;"></span></span><br>
<span class="frame frame-v" style="display:inline-flex;align-items:center;padding:2px;border:2px dashed #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:18px;height:12px;background:#E53935;border:1px solid #888;"></span></span>  (<span style="display:inline-block;width:36px;height:12px;box-sizing:border-box;background:transparent;border:2px dotted #FFFFFF;"></span>)

---

## 10. Question

**toki pona:**  
`jan seme li moku`

*who eats?*

**structure:**  
`{S jan} (seme)`<br>
`|`<br>
`{V moku}`

**colour rendering:**  
`{S Red + Light Blue + Yellow} (dot-fill / static sparkle with irregular dotted frame)`<br>
`|`<br>
`{V Dark Blue + Red}`

**display:**  
<span class="frame frame-s" style="display:inline-flex;align-items:center;padding:2px;border:2px solid #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:12px;height:12px;background:#E53935;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#66CCFF;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:12px;height:12px;background:#F4D03F;border:1px solid #888;"></span></span>  (<span style="display:inline-block;width:36px;height:12px;background:radial-gradient(circle at 8% 10%, #FFFFFF 0 0.5px, transparent 0.7px),radial-gradient(circle at 26% 6%, #FFFFFF 0 0.45px, transparent 0.65px),radial-gradient(circle at 51% 9%, #FFFFFF 0 0.55px, transparent 0.75px),radial-gradient(circle at 74% 7%, #FFFFFF 0 0.5px, transparent 0.7px),radial-gradient(circle at 92% 14%, #FFFFFF 0 0.45px, transparent 0.65px),radial-gradient(circle at 94% 34%, #FFFFFF 0 0.55px, transparent 0.75px),radial-gradient(circle at 92% 56%, #FFFFFF 0 0.5px, transparent 0.7px),radial-gradient(circle at 95% 78%, #FFFFFF 0 0.45px, transparent 0.65px),radial-gradient(circle at 86% 94%, #FFFFFF 0 0.55px, transparent 0.75px),radial-gradient(circle at 62% 94%, #FFFFFF 0 0.5px, transparent 0.7px),radial-gradient(circle at 38% 95%, #FFFFFF 0 0.45px, transparent 0.65px),radial-gradient(circle at 16% 92%, #FFFFFF 0 0.55px, transparent 0.75px),radial-gradient(circle at 5% 72%, #FFFFFF 0 0.5px, transparent 0.7px),radial-gradient(circle at 6% 48%, #FFFFFF 0 0.45px, transparent 0.65px),radial-gradient(circle at 7% 26%, #FFFFFF 0 0.55px, transparent 0.75px),radial-gradient(circle at 30% 30%, #FFFFFF 0 0.5px, transparent 0.7px),radial-gradient(circle at 50% 22%, #FFFFFF 0 0.45px, transparent 0.65px),radial-gradient(circle at 68% 32%, #FFFFFF 0 0.55px, transparent 0.75px),radial-gradient(circle at 36% 54%, #FFFFFF 0 0.5px, transparent 0.7px),radial-gradient(circle at 58% 56%, #FFFFFF 0 0.45px, transparent 0.65px),radial-gradient(circle at 44% 74%, #FFFFFF 0 0.55px, transparent 0.75px),radial-gradient(circle at 12% 18%, #FFFFFF 0 0.5px, transparent 0.7px),radial-gradient(circle at 82% 22%, #FFFFFF 0 0.5px, transparent 0.7px),radial-gradient(circle at 24% 68%, #FFFFFF 0 0.45px, transparent 0.65px),radial-gradient(circle at 72% 84%, #FFFFFF 0 0.55px, transparent 0.75px),radial-gradient(circle at 14% 42%, #FFFFFF 0 0.5px, transparent 0.7px),radial-gradient(circle at 88% 48%, #FFFFFF 0 0.5px, transparent 0.7px),radial-gradient(circle at 46% 10%, #FFFFFF 0 0.45px, transparent 0.65px),radial-gradient(circle at 54% 88%, #FFFFFF 0 0.55px, transparent 0.75px),transparent;"></span>)<br>
<span class="frame frame-v" style="display:inline-flex;align-items:center;padding:2px;border:2px dashed #FFFFFF;border-radius:6px;box-sizing:border-box;vertical-align:middle;"><span class="token" style="display:inline-block;width:18px;height:12px;background:#1E3A8A;border:1px solid #888;"></span><span class="token" style="display:inline-block;width:18px;height:12px;background:#E53935;border:1px solid #888;"></span></span>
