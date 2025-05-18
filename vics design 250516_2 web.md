Jakub Ruzicka | Digital Design Detailing Developer tailwind.config = { darkMode: 'class', theme: { extend: { colors: { primary: { DEFAULT: '#A259FF', 50: '#F5EDFF', 100: '#E9D6FF', 200: '#D2ADFF', 300: '#BC85FF', 400: '#A259FF', 500: '#8A2BE2', 600: '#6A1B9A', 700: '#4B1488', 800: '#320D5E', 900: '#1A0730', }, dark: { DEFAULT: '#0A0A0A', 50: '#F8F8F8', 100: '#E0E0E0', 200: '#C0C0C0', 300: '#A0A0A0', 400: '#808080', 500: '#606060', 600: '#404040', 700: '#202020', 800: '#101010', 900: '#0A0A0A', }, accent: { blue: '#3B82F6', teal: '#2DD4BF', pink: '#EC4899', } }, fontFamily: { sans: \['Inter', 'sans-serif'\], display: \['Inter', 'sans-serif'\], }, animation: { 'float': 'float 6s ease-in-out infinite', 'float-reverse': 'float-reverse 6s ease-in-out infinite', 'fade-in': 'fadeIn 0.8s ease-out forwards', 'text-gradient': 'textGradient 8s ease infinite', 'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite', }, keyframes: { float: { '0%, 100%': { transform: 'translateY(0)' }, '50%': { transform: 'translateY(-20px)' }, }, 'float-reverse': { '0%, 100%': { transform: 'translateY(0)' }, '50%': { transform: 'translateY(20px)' }, }, fadeIn: { '0%': { opacity: '0', transform: 'translateY(20px)' }, '100%': { opacity: '1', transform: 'translateY(0)' }, }, textGradient: { '0%, 100%': { 'background-position': '0% 50%' }, '50%': { 'background-position': '100% 50%' }, } } } } } .gradient-text { background: linear-gradient(90deg, #A259FF 0%, #3B82F6 50%, #2DD4BF 100%); background-size: 200% 200%; -webkit-background-clip: text; background-clip: text; color: transparent; animation: text-gradient 8s ease infinite; } .hero-gradient { background: linear-gradient(135deg, rgba(10, 10, 10, 0.95) 0%, rgba(58, 20, 108, 0.8) 100%); } .glow { box-shadow: 0 0 25px rgba(162, 89, 255, 0.6); } .glow-hover:hover { box-shadow: 0 0 35px rgba(162, 89, 255, 0.8); } .card-hover { transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); } .card-hover:hover { transform: translateY(-10px) scale(1.02); box-shadow: 0 20px 25px -5px rgba(162, 89, 255, 0.1), 0 10px 10px -5px rgba(162, 89, 255, 0.04); } .nav-link { position: relative; } .nav-link:after { content: ''; position: absolute; width: 0; height: 3px; bottom: -5px; left: 0; background: linear-gradient(90deg, #A259FF 0%, #3B82F6 100%); transition: width 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); } .nav-link:hover:after { width: 100%; } .process-step { position: relative; } .process-step:not(:last-child):after { content: ''; position: absolute; top: 40px; right: -60px; width: 40px; height: 3px; background: linear-gradient(90deg, rgba(162, 89, 255, 0.5) 0%, rgba(59, 130, 246, 0.5) 100%); } @media (max-width: 768px) { .process-step:not(:last-child):after { display: none; } } input, textarea, select { transition: all 0.3s ease; } input:focus, textarea:focus, select:focus { outline: none; box-shadow: 0 0 0 3px rgba(162, 89, 255, 0.3); } .animate-delay-100 { animation-delay: 0.1s; } .animate-delay-200 { animation-delay: 0.2s; } .animate-delay-300 { animation-delay: 0.3s; } .animate-delay-400 { animation-delay: 0.4s; } .animate-delay-500 { animation-delay: 0.5s; } .gradient-border { position: relative; background: linear-gradient(135deg, rgba(26, 26, 26, 0.8) 0%, rgba(10, 10, 10, 0.8) 100%); border-radius: 16px; z-index: 1; } .gradient-border::before { content: ''; position: absolute; top: -2px; left: -2px; right: -2px; bottom: -2px; background: linear-gradient(135deg, #A259FF 0%, #3B82F6 100%); border-radius: 18px; z-index: -1; opacity: 0.7; transition: opacity 0.3s ease; } .gradient-border:hover::before { opacity: 1; } .tooltip { position: relative; } .tooltip:hover .tooltip-text { visibility: visible; opacity: 1; transform: translateY(0); } .tooltip-text { visibility: hidden; opacity: 0; position: absolute; z-index: 10; bottom: 125%; left: 50%; transform: translateX(-50%) translateY(10px); background-color: #1A1A1A; color: white; text-align: center; padding: 8px 12px; border-radius: 6px; font-size: 14px; width: max-content; max-width: 200px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); transition: all 0.3s ease; border: 1px solid rgba(255, 255, 255, 0.1); } .tooltip-text::after { content: ""; position: absolute; top: 100%; left: 50%; margin-left: -5px; border-width: 5px; border-style: solid; border-color: #1A1A1A transparent transparent transparent; } .splide\_\_pagination\_\_page.is-active { background: linear-gradient(90deg, #A259FF 0%, #3B82F6 100%) !important; transform: scale(1.2); } .splide\_\_arrow { background: rgba(26, 26, 26, 0.8) !important; border: 1px solid rgba(255, 255, 255, 0.1) !important; opacity: 1 !important; } .splide\_\_arrow:hover { background: rgba(162, 89, 255, 0.2) !important; } .splide\_\_arrow svg { fill: #A259FF !important; }

[

\_

Jakub Ruzicka](#)

- [Services](#services)
- [Work](#work)
- [Process](#process)
- [About](#about)
- [Contact](#contact)

- [Services](#services)
- [Work](#work)
- [Process](#process)
- [About](#about)
- [Contact Us](#contact)

[](#)[](#)[](#)

Next-Gen Digital  
Experiences
==============================

We combine cutting-edge technology with human-centered design to create digital products that drive real business results in today's AI-powered world.

Start Your Project Reference portfolio

[](#services)

![ADAPPT Team](https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800&q=80)

ABOUT US

## Innovating at the Intersection of Tech & Design

adappt represents the evolution of digital innovation. Founded in 2017, we've grown from a small web development shop to a full-service digital transformation agency serving clients worldwide.

Our team of engineers, designers, and strategists are united by a passion for creating digital solutions that not only look beautiful but drive measurable business results. We stay at the forefront of technology trends to ensure our clients always have a competitive edge.

OUR PROCESS

## How We Create Digital Excellence

Our proven methodology ensures we deliver exceptional results at every stage of your project.

#### Discovery

Deep dive into your business goals

#### Strategy

Data-driven solution architecture

#### Design

Human-centered interface creation

#### Development

Agile, iterative implementation

#### Launch & Growth

Optimization and scaling

### Ready to discuss your project?

Schedule a free consultation with our team to explore how we can bring your vision to life with our proven process.

Book a Strategy Call

#### 30-Minute Consultation

Virtual or in-person

#### Expert Guidance

Tailored to your needs

#### No Obligation

Just valuable insights

© 2024 adappt. All rights reserved.

[Privacy Policy](#) [Terms of Service](#) [Cookies](#)

// Preloader // Mobile menu toggle const menuToggle = document.getElementById('menu-toggle'); const mobileMenu = document.getElementById('mobile-menu'); menuToggle.addEventListener('click', () => { mobileMenu.classList.toggle('translate-x-0'); mobileMenu.classList.toggle('translate-x-full'); }); // Close mobile menu when clicking on a link document.querySelectorAll('#mobile-menu a').forEach(link => { link.addEventListener('click', () => { mobileMenu.classList.remove('translate-x-0'); mobileMenu.classList.add('translate-x-full'); }); }); // Smooth scrolling for anchor links document.querySelectorAll('a\[href^="#"\]').forEach(anchor => { anchor.addEventListener('click', function(e) { e.preventDefault(); const targetId = this.getAttribute('href'); if (targetId === '#') return; const targetElement = document.querySelector(targetId); if (targetElement) { window.scrollTo({ top: targetElement.offsetTop - 80, behavior: 'smooth' }); } }); }); // Scroll reveal animations const animateOnScroll = () => { const elements = document.querySelectorAll('.animate-fade-in'); elements.forEach(el => { const elementTop = el.getBoundingClientRect().top; const windowHeight = window.innerHeight; if (elementTop < windowHeight - 100) { el.style.opacity = '1'; } }); }; // Back to top button const backToTopButton = document.getElementById('back-to-top'); window.addEventListener('scroll', () => { animateOnScroll(); // Show/hide back to top button if (window.pageYOffset > 300) { backToTopButton.classList.remove('opacity-0', 'invisible'); backToTopButton.classList.add('opacity-100', 'visible'); } else { backToTopButton.classList.remove('opacity-100', 'visible'); backToTopButton.classList.add('opacity-0', 'invisible'); } }); backToTopButton.addEventListener('click', () => { window.scrollTo({ top: 0, behavior: 'smooth' }); });
