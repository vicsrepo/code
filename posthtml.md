# PostHTML

PostHTML

[PostHTML](https://github.com/posthtml/posthtml) je nástroj pro transformaci HTML pomocí pluginů. PostHTML můžete nakonfigurovat vytvořením konfiguračního souboru s jedním z následujících názvů: `.posthtmlrc` (JSON, **vřele** doporučeno), `.posthtmlrc.js`, `.posthtmlrc.mjs`, `.posthtmlrc.cjs`, `posthtml.config.js`, `posthtml.config.mjs` nebo `posthtml.config.cjs`.

Nainstalujte pluginy do vašeho projektu:

```bash
yarn add posthtml-doctype --dev
```

Poté vytvořte konfigurační soubor:

Pluginy jsou specifikovány v objektu plugins jako klíče a možnosti jsou definovány jako hodnoty objektu. Pokud pro plugin nejsou žádné možnosti, stačí nastavit prázdný objekt.

Tento příklad využívá [posthtml-include](https://github.com/posthtml/posthtml-include) pro vložení dalšího HTML souboru.
