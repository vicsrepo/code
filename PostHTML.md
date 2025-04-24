PostHTML

[PostHTML](https://github.com/posthtml/posthtml) je nástroj pro transformaci HTML pomocí pluginů. PostHTML můžete nakonfigurovat vytvořením konfiguračního souboru s jedním z následujících názvů: `.posthtmlrc` (JSON, **vřele** doporučeno), `.posthtmlrc.js`, `.posthtmlrc.mjs`, `.posthtmlrc.cjs`, `posthtml.config.js`, `posthtml.config.mjs` nebo `posthtml.config.cjs`.

Nainstalujte pluginy do vašeho projektu:

```bash
yarn add posthtml-doctype --dev
```

Poté vytvořte konfigurační soubor:

{% sample %}
{% samplefile ".posthtmlrc" %}

```json
{
  "plugins": {
    "posthtml-doctype": { "doctype": "HTML 5" }
  }
}
```

{% endsamplefile %}
{% endsample %}

Pluginy jsou specifikovány v objektu plugins jako klíče a možnosti jsou definovány jako hodnoty objektu. Pokud pro plugin nejsou žádné možnosti, stačí nastavit prázdný objekt.

Tento příklad využívá [posthtml-include](https://github.com/posthtml/posthtml-include) pro vložení dalšího HTML souboru.

{% sample %}
{% samplefile ".posthtmlrc" %}

```json
{
  "plugins": {
    "posthtml-include": {}
  }
}
```

{% endsamplefile %}
{% samplefile "index.html" %}

```html
<html>
  <head>
    <title>Domovská stránka</title>
  </head>
  <body>
    <include src="header.html"></include>
    <main>Můj obsah</main>
  </body>
</html>
```

{% endsamplefile %}
{% samplefile "header.html" %}

```html
<header>Toto je moje hlavička</header>
```

{% endsamplefile %}
{% endsample %}
