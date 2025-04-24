# Úvod (Introduction)

Fetch API v JavaScriptu umožňuje načítat data asynchronně ze serveru, včetně HTML segmentů uložených v samostatných souborech. Tento přístup je užitečný pro rozdělení webu na menší komponenty (např. header, footer, obsah), které se dynamicky načítají do hlavního souboru `index.html`. Zlepšuje to udržovatelnost kódu a umožňuje opětovné použití komponent.

## Použití (Usage)

- **Základní princip**: Pomocí `fetch()` načtete obsah HTML souboru a vložíte ho do DOM pomocí `innerHTML` nebo jiných metod.
- **Asynchronní operace**: Fetch pracuje asynchronně, takže neblokuje vykreslování stránky.
- **Zpracování chyb**: Vždy ošetřete chyby pomocí `.catch()` nebo `try/catch` u `async/await`.

## Příklady (Examples)

### 1. Načtení jednoho segmentu (`header.html → index.html`)

**Struktura souborů:**

```
project/
├── index.html
├── header.html
└── script.js
```

**`header.html`:**

```html
<header>
    <h1>Můj web</h1>
    <nav>
        <a href="/">Domů</a>
        <a href="/o-nas">O nás</a>
    </nav>
</header>
```

**`script.js`:**

```javascript
// Načtení header.html a vložení do elementu s id="header-container"
fetch('header.html')
    .then(response => response.text())
    .then(html => {
        document.getElementById('header-container').innerHTML = html;
    })
    .catch(error => console.error('Chyba při načítání headeru:', error));
```

**`index.html`:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Dynamic Loading Example</title>
</head>
<body>
    <div id="header-container"></div> <!-- Zde se zobrazí header -->
    <script src="script.js"></script>
</body>
</html>
```

---

### 2. Načtení více segmentů (`header`, `content`, `footer`)

**`script.js`:**

```javascript
// Funkce pro načtení a vložení HTML
function loadComponent(url, elementId) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById(elementId).innerHTML = html;
        })
        .catch(error => console.error(`Chyba při načítání ${url}:`, error));
}

// Načtení všech komponent
loadComponent('header.html', 'header-container');
loadComponent('content.html', 'content-container');
loadComponent('footer.html', 'footer-container');
```

**`index.html`:**

```html
<body>
    <div id="header-container"></div>
    <div id="content-container"></div>
    <div id="footer-container"></div>
    <script src="script.js"></script>
</body>
```

---

### 3. Dynamické načítání obsahu (např. při kliknutí na odkaz)

**`script.js`:**

```javascript
document.querySelectorAll('a[data-page]').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const page = e.target.dataset.page; // např. 'o-nas.html'
        
        fetch(page)
            .then(response => response.text())
            .then(html => {
                document.getElementById('content-container').innerHTML = html;
            })
            .catch(error => console.error('Chyba:', error));
    });
});
```

**`index.html`:**

```html
<a href="#" data-page="o-nas.html">O nás</a>
<div id="content-container"></div>
```

---

## Důležité poznámky

- **CORS**: Pokud testujete lokálně, spusťte soubory přes server (např. pomocí Live Server ve VS Code), jinak Fetch nebude fungovat kvůli bezpečnostním omezením.
- **SEO**: Dynamicky načtený obsah nemusí být indexován vyhledávači. Pro kritické části použijte server-side rendering.
- **Progresivní vylepšení**: Pro starší prohlížeče přidejte polyfill pro Fetch API.

Tento přístup je ideální pro jednoduché weby nebo prototypy. Pro složitější projekty zvažte frameworky jako React nebo Vue.js.