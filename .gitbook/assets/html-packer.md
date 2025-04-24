# Přehled alternativ k nástroji html-packer

Níže uvádím přehled několika alternativ k nástroji **html-packer**, který byl vyvinut jako rozšíření původního projektu _inline-source_. Cílem je vytvořit jediný HTML soubor s vloženými skripty, styly, obrázky (včetně SVG) a zároveň provést jejich minifikaci. Každá z alternativ má své výhody a specifika – zde najdete podrobný přehled:

## 1. inline-source

**Co to je:**  
_Nástroj_, který přečte HTML soubor, najde tagy jako `<script>`, `<link>` a `<img>` a nahradí odkazy obsahem (např. vloží obsah CSS a JS přímo do stránky nebo zakóduje obrázek do base64).

**Výhody:**

- Osvědčené řešení s aktivní komunitou uživatelů; lze případně rozšířit či modifikovat podle potřeby.
- Snadná integrace do automatizačního build procesu.

**Kdy jej použít:**  
Pro jednoduchý a konfigurovatelný nástroj pro inlineování zdrojů, zejména pokud preferujete rozšíření původního řešení namísto zásadních úprav html-packeru.

## 2. pack-html (Skinner927/pack-html)

**Co to je:**  
Projekt, který načte HTML dokument a vloží všechny externí zdroje (skripty, styly, obrázky) přímo do HTML. Podporuje zpracování URL v CSS, což umožňuje zakódování obrázků do base64.

**Výhody:**

- Podpora pro komplexnější scénáře inlinování (např. zpracování URL v CSS).
- Možnost minifikace výsledného souboru.

**Kdy jej použít:**  
Pokud hledáte robustnější zpracování zdrojů, aniž byste museli vyvíjet vlastní řešení, nebo preferujete jiný programovací jazyk.

## 3. Gulp pluginy a task-runnerová řešení

**Co to je:**  
Pro prostředí využívající nástroje jako Gulp existují pluginy jako `gulp-inline-source` nebo `gulp-inline`, které dynamicky vkládají obsah externích souborů přímo do HTML.

**Výhody:**

- Snadná integrace do stávajícího front-end build systému.
- Přizpůsobení a řetězení dalších úloh (minifikace, revize souborů, cache busting).

**Kdy jej použít:**  
Pokud již máte build proces založený na Gulp, tyto pluginy umožní nahradit externí odkazy obsahem bez potřeby samostatného CLI nástroje.

## 4. SingleFile

**Co to je:**  
Rozšíření pro webové prohlížeče (Chrome, Firefox a další), které umožňuje uložit aktuální webovou stránku jako jediný samostatný HTML soubor s veškerým obsahem (JavaScript, CSS, obrázky) vloženým do dokumentu.

**Výhody:**

- Rychlé a snadné uložení či archivace stránky přímo z prohlížeče.
- Kompletně samostatný HTML soubor, vhodný pro sdílení či archivaci.

**Kdy jej použít:**  
Pro archivaci nebo sdílení webové stránky bez nastavování build systému, ideální pro interaktivní použití.

## 5. Monolith

**Co to je:**  
Nástroj (často psaný v jazycích jako Rust či Go), který uloží celou webovou stránku včetně zdrojů do jednoho HTML souboru. Používá se zejména pro archivaci webu.

**Výhody:**

- Generuje jediný soubor se všemi potřebnými zdroji, podobně jako SingleFile.
- Possible nasazení jako CLI nástroj pro automatické archivní skripty nebo serverové použití.

**Kdy jej použít:**  
Pokud hledáte robustní řešení pro archivaci webových stránek pro offline prohlížení či archivaci, které běží jako samostatný CLI nástroj.

---

### Shrnutí

Každá alternativa nabízí odlišný přístup:

- **inline-source:** Ideální, pokud vyhovuje jednoduché a rozšiřitelné řešení.
- **pack-html:** Vhodná pro situace vyžadující komplexnější úpravy (např. zpracování URL v CSS).
- **Gulp pluginy:** Dobrá volba, pokud již využíváte build systém založený na Gulp.
- **SingleFile a Monolith:** Skvělé pro archivaci stránek nebo rychlé zabalování webu přímo z prohlížeče/CLI.

Při výběru správné alternativy zvažte, zda preferujete integraci do automatizovaného build systému, nebo spíše interaktivní řešení pro ukládání a archivaci.

Máte-li další otázky nebo potřebujete specifikovat funkce (např. podpora minifikace, vlastní rozšíření či možnost přizpůsobení), dejte vědět.
