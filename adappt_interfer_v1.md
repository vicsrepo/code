```markdown
# ADAPPT – Digitální agentura

## Úvod
ADAPPT je digitální agentura zaměřená na vývoj webu, branding a marketingové strategie. Tento projekt je moderní přepis statické HTML stránky do modulárního prostředí pomocí **Vite + TypeScript**.

---

## Struktura projektu

```
adappt-vite/
├── index.html
├── README.md
├── tsconfig.json
├── vite.config.ts
├── package.json
├── src/
│   ├── main.ts
│   ├── styles/
│   │   └── style.css
│   ├── components/
│   │   ├── Header.ts
│   │   ├── Hero.ts
│   │   ├── Services.ts
│   │   ├── WhyAdappt.ts
│   │   └── Footer.ts
│   └── utils/
│       └── theme.ts
```

---

## Obsah souborů

### `index.html`
```html
<!DOCTYPE html>
<html lang="cs">
    <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/vite.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>ADAPPT - Digitální agentura</title>
    </head>
    <body>
        <div id="app"></div>
        <script type="module" src="/src/main.ts"></script>
    </body>
</html>
```

### `package.json`
```json
{
    "name": "adappt-vite",
    "version": "1.0.0",
    "scripts": {
        "dev": "vite",
        "build": "vite build",
        "preview": "vite preview"
    },
    "devDependencies": {
        "typescript": "^5.3.3",
        "vite": "^5.0.0"
    }
}
```

### `tsconfig.json`
```json
{
    "compilerOptions": {
        "target": "ESNext",
        "module": "ESNext",
        "moduleResolution": "Node",
        "strict": true,
        "jsx": "preserve",
        "esModuleInterop": true,
        "forceConsistentCasingInFileNames": true,
        "skipLibCheck": true,
        "resolveJsonModule": true,
        "isolatedModules": true,
        "lib": ["DOM", "ESNext"]
    },
    "include": ["src"]
}
```

### `vite.config.ts`
```ts
import { defineConfig } from 'vite'

export default defineConfig({
    server: {
        port: 5173
    }
})
```

### `src/main.ts`
```ts
import './styles/style.css'
import { renderHeader } from './components/Header'
import { renderHero } from './components/Hero'
import { renderServices } from './components/Services'
import { renderWhyAdappt } from './components/WhyAdappt'
import { renderFooter } from './components/Footer'
import { toggleTheme, changeLang, applySavedTheme } from './utils/theme'

document.addEventListener('DOMContentLoaded', () => {
    applySavedTheme()

    const app = document.querySelector<HTMLDivElement>('#app')!
    app.append(
        renderHeader(),
        renderHero(),
        renderServices(),
        renderWhyAdappt(),
        renderFooter()
    )

    document.getElementById('themeToggle')?.addEventListener('click', toggleTheme)
    document.getElementById('langToggle')?.addEventListener('click', changeLang)
})
```

### `src/components/Header.ts`
```ts
export function renderHeader(): HTMLElement {
    const header = document.createElement('header')
    header.innerHTML = `
        <div class="logo">ADAPPT</div>
        <nav class="desktop-nav">
            <a href="#">Domů</a>
            <a href="#">Služby</a>
            <a href="#">Projekty</a>
            <a href="#">Blog</a>
            <a href="#">Kontakt</a>
        </nav>
        <div class="toggle-btns">
            <button class="btn" id="themeToggle">🌓 Režim</button>
            <button class="btn" id="langToggle">🌐 CZ</button>
        </div>
    `
    return header
}
```

### `src/components/Hero.ts`
```ts
export function renderHero(): HTMLElement {
    const section = document.createElement('section')
    section.className = 'hero'
    section.innerHTML = `
        <h1>Transformujeme digitální zážitky</h1>
        <p>ADAPPT je digitální agentura, která přináší efektivní řešení v oblasti webového vývoje, designu, brandingu a marketingu.</p>
    `
    return section
}
```

### `src/components/Services.ts`
```ts
export function renderServices(): HTMLElement {
    const section = document.createElement('section')
    section.className = 'grid'
    section.innerHTML = `
        <div class="card">
            <h3>Webový vývoj</h3>
            <p>Na míru šité weby optimalizované pro výkon, responzivitu a škálovatelnost.</p>
        </div>
        <div class="card">
            <h3>Identita značky</h3>
            <p>Silná vizuální identita a sdělení, která vyniknou v digitálním světě.</p>
        </div>
        <div class="card">
            <h3>UI/UX design</h3>
            <p>Intuitivní a elegantní rozhraní pro bezproblémový uživatelský zážitek.</p>
        </div>
        <div class="card">
            <h3>Digitální marketing</h3>
            <p>Strategie založené na datech pro zvýšení zapojení, leadů a konverzí.</p>
        </div>
    `
    return section
}
```

### `src/components/WhyAdappt.ts`
```ts
export function renderWhyAdappt(): HTMLElement {
    const section = document.createElement('section')
    section.className = 'why-section'
    section.innerHTML = `
        <h2>Proč právě ADAPPT?</h2>
        <div class="features">
            <div class="feature">
                <h4>Škálovatelné řešení</h4>
                <p>Navržené pro růst – postavené na moderních technologiích a osvědčených postupech.</p>
            </div>
            <div class="feature">
                <h4>Kreativní i technické</h4>
                <p>Spojujeme estetiku s chytrým vývojem pro nezapomenutelný výsledek.</p>
            </div>
            <div class="feature">
                <h4>Připraveno na budoucnost</h4>
                <p>Web3, AI a nové technologie – strategicky integrované.</p>
            </div>
            <div class="feature">
                <h4>Zaměření na klienta</h4>
                <p>Spolupráce jako partnerství – vaše cíle jsou i našimi.</p>
            </div>
        </div>
    `
    return section
}
```

### `src/components/Footer.ts`
```ts
export function renderFooter(): HTMLElement {
    const footer = document.createElement('footer')
    footer.innerHTML = `
        &copy; 2025 ADAPPT. Všechna práva vyhrazena. |
        <a href="#">Ochrana osobních údajů</a> |
        <a href="#">Podmínky použití</a>
    `
    return footer
}
```

### `src/utils/theme.ts`
```ts
export function toggleTheme() {
    const current = document.body.getAttribute('data-theme') || 'dark'
    const next = current === 'dark' ? 'light' : 'dark'
    document.body.setAttribute('data-theme', next)
    localStorage.setItem('theme', next)
}

export function changeLang() {
    const btn = document.getElementById('langToggle')
    if (btn) {
        btn.textContent = btn.textContent.includes('CZ') ? '🌐 EN' : '🌐 CZ'
    }
}

export function applySavedTheme() {
    const savedTheme = localStorage.getItem('theme') || 'dark'
    document.body.setAttribute('data-theme', savedTheme)
}
```

---

## 💻 Instalace & spuštění

1. Stáhni nebo naklonuj repozitář.
2. Spusť následující příkazy v terminálu:

```bash
npm install
npm run dev
```

3. Otevři prohlížeč na adrese: `http://localhost:5173`.

---

## 🔧 Připravené funkce

- **Tmavý/světlý režim**: Přepínání mezi režimy s uložením do `localStorage`.
- **Přepínač jazyka**: CZ/EN (zatím pouze textově).
- **Responzivní design**: Optimalizováno pro mobilní zařízení.
- **Modularita**: Snadné přidávání nových komponent.

---

## 📌 Možnosti rozšíření

- Přidání formuláře s validací.
- Napojení na CMS (např. Sanity, Storyblok).
- Překlady pomocí i18next.
- SEO optimalizace.

---

Dej vědět, pokud potřebuješ další úpravy nebo rozšíření! 🚀
```
