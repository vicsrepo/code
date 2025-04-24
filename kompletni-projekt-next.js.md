# Kompletní projekt Next.js

Níže naleznete podrobný návod, jak rozdělit velký HTML soubor do jednotlivých komponent v prostředí (například pomocí Next.js nebo Reactu) a jak takový projekt strukturovat. Tento příklad zahrnuje oddělení hlavičky, hero sekce, služeb, USP (unique selling points), procesu, patičky a implementaci efektů (smooth scrolling a scroll animace) pomocí efektů v Reactu.

## 1. Vytvoření projektu a struktury adresářů

Pokud ještě nemáte nastavený projekt, můžete použít například Next.js. Vytvořte nový projekt pomocí Create Next App:

```bash
npx create-next-app@latest my-adappt-project
cd my-adappt-project
```

Struktura projektu:

```
my-adappt-project/
├── components/
│   ├── Footer.jsx
│   ├── Header.jsx
│   ├── Hero.jsx
│   ├── Process.jsx
│   ├── ScrollAnimations.jsx
│   ├── Services.jsx
│   └── USP.jsx
├── pages/
│   ├── _app.js
│   └── index.js
├── styles/
│   └── globals.css
└── package.json
```

## 2. Globální styly

Vytvořte soubor `styles/globals.css` a vložte do něj veškeré CSS styly:

```css
/* styles/globals.css */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Inter", sans-serif;
  background: #0a0a0a;
  color: #fff;
}

header {
  display: flex;
  justify-content: space-between;
  padding: 20px 80px;
  align-items: center;
  background-color: rgba(10, 10, 10, 0.9);
  position: fixed;
  width: 100%;
  z-index: 1000;
}

.logo {
  font-size: 24px;
  font-weight: bold;
  letter-spacing: 2px;
  color: #a259ff;
}

nav ul {
  display: flex;
  list-style: none;
  gap: 40px;
}

nav a {
  color: #fff;
  text-decoration: none;
  font-size: 16px;
  transition: color 0.3s ease;
}

nav a:hover {
  color: #a259ff;
}

.contact-btn {
  background: #a259ff;
  padding: 12px 24px;
  border-radius: 8px;
  transition: transform 0.3s ease;
}

.contact-btn:hover {
  transform: translateY(-2px);
}

.hero {
  padding: 200px 20px 150px;
  text-align: center;
  background: linear-gradient(rgba(10, 10, 10, 0.7), rgba(10, 10, 10, 0.7)),
    url("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1920&q=80");
  background-size: cover;
  background-position: center;
}

.hero h1 {
  font-size: 64px;
  font-weight: 900;
  letter-spacing: -2px;
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.1;
}

.hero p {
  margin-top: 30px;
  color: #b0b0b0;
  font-size: 20px;
  max-width: 600px;
  margin: 30px auto;
  line-height: 1.6;
}

.cta-buttons {
  margin-top: 50px;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.cta-btn {
  padding: 16px 32px;
  border-radius: 8px;
  font-size: 16px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.primary-cta {
  background: #a259ff;
  border: none;
  color: white;
}

.secondary-cta {
  border: 2px solid #a259ff;
  background: transparent;
  color: #a259ff;
}

.cta-btn:hover {
  transform: translateY(-3px);
}

.section-title {
  text-align: center;
  font-size: 36px;
  margin-bottom: 60px;
  padding-top: 80px;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
  padding: 0 80px 80px;
  max-width: 1200px;
  margin: 0 auto;
}

.service-card {
  background: #1a1a1a;
  padding: 40px;
  border-radius: 16px;
  text-align: center;
  transition: transform 0.3s ease;
}

.service-card:hover {
  transform: translateY(-10px);
}

.service-icon {
  font-size: 40px;
  margin-bottom: 20px;
}

.usp-section {
  background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
  padding: 80px 20px;
}

.usp-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

.usp-card {
  background: rgba(255, 255, 255, 0.05);
  padding: 30px;
  border-radius: 16px;
  border: 1px solid rgba(162, 89, 255, 0.2);
}

.process-steps {
  display: flex;
  justify-content: center;
  gap: 40px;
  padding: 0 20px 80px;
  flex-wrap: wrap;
}

.process-step {
  width: 200px;
  text-align: center;
}

.process-step .icon {
  font-size: 32px;
  margin-bottom: 20px;
  color: #a259ff;
}

footer {
  text-align: center;
  padding: 60px 0;
  background: #1a1a1a;
  margin-top: 80px;
}
```

V souboru `pages/_app.js` (nebo `_app.tsx` pro TypeScript) nezapomeňte importovat globální styly:

```jsx
// pages/_app.js
import "../styles/globals.css";

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

## 3. Vytvoření jednotlivých komponent

### 3.1 Header

Vytvořte soubor `components/Header.jsx`:

```jsx
// components/Header.jsx
const Header = () => {
  return (
    <header>
      <div className="logo">ADAPPT</div>
      <nav>
        <ul>
          <li>
            <a href="#services">Services</a>
          </li>
          <li>
            <a href="#work">Work</a>
          </li>
          <li>
            <a href="#process">Process</a>
          </li>
          <li>
            <a href="#contact" className="contact-btn">
              Contact
            </a>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
```

### 3.2 Hero sekce

Vytvořte soubor `components/Hero.jsx`:

```jsx
// components/Hero.jsx
const Hero = () => {
  return (
    <section className="hero">
      <h1>ADAPPT – Digital Experiences, Designed to Evolve</h1>
      <p>
        We help startups and enterprises scale and succeed through expert web
        development, compelling branding, intuitive UI/UX, and data-driven
        marketing.
      </p>
      <div className="cta-buttons">
        <button className="cta-btn primary-cta">Let's Build Together</button>
        <button className="cta-btn secondary-cta">View Our Work</button>
      </div>
    </section>
  );
};

export default Hero;
```

### 3.3 Služby (Services)

Vytvořte soubor `components/Services.jsx`:

```jsx
// components/Services.jsx
const Services = () => {
  return (
    <section id="services">
      <h2 className="section-title">What We Do Best</h2>
      <div className="services-grid">
        <div className="service-card">
          <div className="service-icon">🌐</div>
          <h3>Web Development</h3>
          <p>
            Responsive websites and scalable platforms built to meet today’s and
            tomorrow’s demands.
          </p>
        </div>
        <div className="service-card">
          <div className="service-icon">🎨</div>
          <h3>Brand Identity</h3>
          <p>
            Crafting distinct brands with strategy, narrative, and visuals that
            resonate.
          </p>
        </div>
        <div className="service-card">
          <div className="service-icon">📱</div>
          <h3>UI/UX Design</h3>
          <p>
            Designing human-first interfaces that convert visitors into loyal
            users.
          </p>
        </div>
        <div className="service-card">
          <div className="service-icon">📣</div>
          <h3>Digital Marketing</h3>
          <p>
            Data-backed campaigns designed to drive growth and measurable
            success.
          </p>
        </div>
      </div>
    </section>
  );
};

export default Services;
```

### 3.4 USP sekce

Vytvořte soubor `components/USP.jsx`:

```jsx
// components/USP.jsx
const USP = () => {
  return (
    <section className="usp-section">
      <h2 className="section-title">Why Choose ADAPPT</h2>
      <div className="usp-grid">
        <div className="usp-card">
          <h3>🧩 Scalable Solutions</h3>
          <p>
            Our platforms are built with growth in mind—from MVP to
            enterprise-level applications.
          </p>
        </div>
        <div className="usp-card">
          <h3>🎯 Creative Meets Technical</h3>
          <p>
            We merge visionary design with technical precision for robust,
            striking solutions.
          </p>
        </div>
        <div className="usp-card">
          <h3>🔮 Future-Ready</h3>
          <p>
            Constantly innovating to keep you ahead in a dynamic digital
            landscape.
          </p>
        </div>
        <div className="usp-card">
          <h3>🤝 Client-Centric Approach</h3>
          <p>
            Your vision steers every step; collaboration and transparency are
            core to our process.
          </p>
        </div>
      </div>
    </section>
  );
};

export default USP;
```

### 3.5 Proces

Vytvořte soubor `components/Process.jsx`:

```jsx
// components/Process.jsx
const Process = () => {
  return (
    <section id="process">
      <h2 className="section-title">Our Process</h2>
      <div className="process-steps">
        <div className="process-step">
          <div className="icon">🎯</div>
          <h4>Discovery</h4>
          <p>Immersive sessions to understand your business goals</p>
        </div>
        <div className="process-step">
          <div className="icon">🧠</div>
          <h4>Strategy</h4>
          <p>Detailed planning for user flows and architecture</p>
        </div>
        <div className="process-step">
          <div className="icon">🎨</div>
          <h4>Design</h4>
          <p>Wireframes to polished, conversion-focused visuals</p>
        </div>
        <div className="process-step">
          <div className="icon">🛠️</div>
          <h4>Development</h4>
          <p>Agile development with transparent updates</p>
        </div>
        <div className="process-step">
          <div className="icon">📈</div>
          <h4>Launch & Growth</h4>
          <p>Continuous optimization and support</p>
        </div>
      </div>
    </section>
  );
};

export default Process;
```

### 3.6 Patička (Footer)

Vytvořte soubor `components/Footer.jsx`:

```jsx
// components/Footer.jsx
const Footer = () => {
  return (
    <footer>
      <p>© 2024 ADAPPT – Digital Experiences, Designed to Evolve</p>
    </footer>
  );
};

export default Footer;
```

### 3.7 Scroll Animations a Smooth Scrolling

Vytvořte soubor `components/ScrollAnimations.jsx`:

```jsx
// components/ScrollAnimations.jsx
import { useEffect } from "react";

const ScrollAnimations = () => {
  useEffect(() => {
    // Smooth scrolling pro anchor odkazy
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        e.preventDefault();
        const targetId = anchor.getAttribute("href");
        const target = document.querySelector(targetId);
        if (target) {
          target.scrollIntoView({ behavior: "smooth" });
        }
      });
    });

    // Animace při scrollování pomocí IntersectionObserver
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = 1;
          entry.target.style.transform = "translateY(0)";
        }
      });
    });

    const animatedElements = document.querySelectorAll(
      ".service-card, .usp-card, .process-step"
    );
    animatedElements.forEach((el) => {
      el.style.opacity = 0;
      el.style.transform = "translateY(20px)";
      el.style.transition = "all 0.6s ease-out";
      observer.observe(el);
    });

    // Cleanup: odstranění event listenerů (pokud je to potřeba)
    return () => {
      anchorLinks.forEach((anchor) => {
        anchor.removeEventListener("click", () => {});
      });
    };
  }, []);

  return null;
};

export default ScrollAnimations;
```

## 4. Hlavní stránka

V souboru `pages/index.js` pospojíte všechny komponenty:

```jsx
// pages/index.js
import Header from "../components/Header";
import Hero from "../components/Hero";
import Services from "../components/Services";
import USP from "../components/USP";
import Process from "../components/Process";
import Footer from "../components/Footer";
import ScrollAnimations from "../components/ScrollAnimations";

export default function Home() {
  return (
    <>
      <Header />
      <Hero />
      <Services />
      <USP />
      <Process />
      <Footer />
      <ScrollAnimations />
    </>
  );
}
```

## 5. package.json

Konfigurační soubor projektu:

```json
{
  "name": "my-adappt-project",
  "version": "1.0.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest"
  }
}
```

Tímto způsobem dosáhnete čistého a modulárního kódu, kde je každý blok HTML oddělen do samostatné komponenty a interaktivita je řešena pomocí React hooků.

Nyní máte kompletní projekt, který si můžete stáhnout jako ZIP soubor.
