# tailwind

md## Dokumentace k Tailwind CSS Frameworku

#### Úvod

Tailwind CSS je utility-first CSS framework pro rychlý vývoj moderních webových rozhraní. Na rozdíl od tradičních CSS frameworků jako Bootstrap nebo Foundation, Tailwind neposkytuje předem navržené komponenty. Místo toho nabízí nízkoúrovňové utility třídy, které umožňují vytvářet vlastní designy bez nutnosti psaní vlastního CSS.

#### Proč používat Tailwind CSS?

* **Rychlejší vývoj**: Použitím utility tříd se dá velmi rychle stylovat HTML prvky bez přepínání mezi HTML a CSS soubory.
* **Vyšší konzistence**: Díky předdefinovaným třídám je design konzistentní napříč celou aplikací.
* **Snadné přizpůsobení**: Tailwind je vysoce konfigurovatelný skrze konfigurační soubor `tailwind.config.js`.
* **Malý výsledný CSS soubor**: S nástroji jako PurgeCSS se odstraní nepoužité třídy, čímž se minimalizuje výsledná velikost CSS.

#### Instalace

Tailwind CSS lze nainstalovat několika způsoby. Nejčastěji se používá přes npm:

```bash
npm install -D tailwindcss
npx tailwindcss init
```

Tímto příkazem se vytvoří základní konfigurační soubor `tailwind.config.js`, který lze upravit dle potřeby.

#### Struktura a architektura

Tailwind je postaven na principu utility-first. Místo psaní vlastních CSS tříd jako:

```css
.btn {
  background-color: blue;
  padding: 1rem;
  color: white;
}
```

... se přímo v HTML používají utility třídy:

```html
<button class="bg-blue-500 px-4 py-2 text-white">Klikni mě</button>
```

#### Základní utility třídy

Tailwind nabízí stovky utility tříd pokrývajících:

* Barvy (`bg-*`, `text-*`, `border-*`)
* Rozměry (`w-*`, `h-*`, `max-w-*`)
* Mezera (`m-*`, `p-*`, `space-x-*`, `space-y-*`)
* Flexbox a Grid (`flex`, `grid`, `items-center`, `justify-between`)
* Typografie (`text-*`, `font-*`, `leading-*`, `tracking-*`)
* Stavy (`hover:*`, `focus:*`, `disabled:*`)

#### Responzivita

Tailwind má zabudovaný systém pro tvorbu responzivních designů. Pomocí prefixů lze stylovat podle breakpointů:

```html
<div class="text-sm md:text-lg lg:text-xl">Text</div>
```

#### Variants a pseudo-třídy

Každá utility třída může být rozšířena o varianty jako `hover:`, `focus:`, `active:`, `disabled:` atd.:

```html
<button class="bg-blue-500 hover:bg-blue-700">Tlačítko</button>
```

#### Customizace

V `tailwind.config.js` lze přizpůsobit téměř cokoliv:

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#1da1f2',
      },
      spacing: {
        '72': '18rem',
        '84': '21rem',
      },
    },
  },
}
```

#### Tvorba komponent

Ačkoli Tailwind není komponentový framework, lze snadno tvořit znovupoužitelné komponenty pomocí utility tříd a šablonovacích jazyků jako Blade, JSX nebo jiných.

#### Pluginy

Tailwind podporuje pluginy. Například plugin pro formuláře:

```bash
npm install @tailwindcss/forms
```

V `tailwind.config.js`:

```js
plugins: [
  require('@tailwindcss/forms'),
]
```

#### Build proces

Tailwind CSS využívá PostCSS a má vlastní CLI nástroj:

```bash
npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch
```

#### PurgeCSS / Content-based pruning

Tailwind pro produkční build odstraňuje nepoužité styly:

```js
module.exports = {
  content: ['./public/**/*.html', './src/**/*.js'],
  // ...
}
```

#### Integrace s frameworky

Tailwind lze snadno integrovat s:

* React
* Vue
* Angular
* Next.js
* Nuxt.js
* Laravel
* Svelte

#### Porovnání s jinými frameworky

| Funkce         | Tailwind CSS    | Bootstrap | Bulma    |
| -------------- | --------------- | --------- | -------- |
| Utility-first  | Ano             | Ne        | Částečně |
| Konfigurace    | Vysoce          | Omezená   | Omezená  |
| Velikost build | Malá (po purge) | Střední   | Střední  |
| Responzivita   | Výborná         | Výborná   | Dobrá    |

#### Případové studie

(sem mohou být doplněny konkrétní příklady použití Tailwindu ve firmách nebo projektech)

#### Dark Mode

Tailwind má podporu pro dark mode, kterou lze aktivovat v konfiguraci:

```js
module.exports = {
  darkMode: 'class', // nebo 'media'
  // ...
}
```

Použití v HTML:

```html
<body class="dark">
  <div class="bg-white dark:bg-gray-800 text-black dark:text-white">
    Obsah
  </div>
</body>
```

#### Přístupnost

Tailwind podporuje tvorbu přístupných rozhraní, ale zodpovědnost za správnou strukturu a atributy je na vývojáři. Doporučuje se používat:

* `aria-*` atributy
* semantic HTML značky
* dostatečný kontrast mezi textem a pozadím

#### Testování stylů

Přímé testování CSS v Tailwindu je obtížnější kvůli absenci vlastních tříd. Doporučuje se testovat funkcionalitu komponent a snapshot testy, případně přímé ověření hodnot stylů.

#### Tipy a best practices

* Používejte komponentový přístup – vytvářejte části UI jako partials.
* Preferujte `@apply` v případě opakujících se vzorů.
* Sledujte velikost výstupního CSS.
* Mějte přehled o dostupných utilitách – Tailwind dokumentace je skvělý zdroj.

#### Bezpečnostní hlediska

Tailwind sám o sobě nepředstavuje bezpečnostní riziko, ale jeho dynamické generování tříd může být problém při použití s některými šablonovacími enginy (např. ve Vue nebo Blade). Vždy whitelistujte dynamicky generované třídy nebo použijte `safelist`.

#### Budoucnost a roadmapa

Tailwind se aktivně vyvíjí, s důrazem na výkon, použitelnost a nástroje jako Tailwind UI nebo Headless UI. Vývojáři mohou očekávat další zlepšení jako lepší podpora pro theming, animace a ještě hlubší integraci do frontend ekosystému.

#### Závěr

Tailwind CSS je výkonný nástroj pro vývoj moderních rozhraní. Díky utility-first přístupu zvyšuje rychlost vývoje, udržuje kód konzistentní a umožňuje rozsáhlou přizpůsobitelnost bez nutnosti psaní složitých CSS souborů.

Tato dokumentace je navržena jako přehledový průvodce i podrobný manuál. Další části mohou zahrnovat pokročilé příklady integrací, CI/CD buildy, nástroje třetích stran a real-world případy použití.
