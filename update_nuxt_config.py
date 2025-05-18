# update_nuxt_config.py
# Skript, který zajistí, že `nuxt.config.ts` obsahuje app.payload.replacer pro odstranění funkcí
import re
import sys
from pathlib import Path

def insert_full_app_block(content: str) -> str:
    # Vloží celý blok app/payload za defineNuxtConfig({
    block = (
        "defineNuxtConfig({\n"
        "  app: {\n"
        "    payload: {\n"
        "      replacer: (key, value) => {\n"
        "        if (typeof value === 'function') {\n"
        "          return undefined;\n"
        "        }\n"
        "        return value;\n"
        "      }\n"
        "    }\n"
        "  },"
    )
    return re.sub(r"defineNuxtConfig\(\{", block, content, count=1)

def insert_payload_into_app(content: str) -> str:
    # Vloží payload blok dovnitř existující sekce app
    def repl(match):
        indent = match.group(1)
        return (match.group(0) + f"\n{indent}  payload: {{\n"
                                  f"{indent}    replacer: (key, value) => {{\n"
                                  f"{indent}      if (typeof value === 'function') {{\n"
                                  f"{indent}        return undefined;\n"
                                  f"{indent}      }}\n"
                                  f"{indent}      return value;\n"
                                  f"{indent}    }}\n"
                                  f"{indent}  }}",
                      )
    return re.sub(r"(app\s*:\s*{)", repl, content, count=1)

def main(path_str='nuxt.config.ts'):
    path = Path(path_str)
    if not path.exists():
        print(f"Chyba: Soubor '{path_str}' nebyl nalezen.")
        sys.exit(1)

    content = path.read_text(encoding='utf-8')

    if 'replacer:' in content:
        print("Sekce payload.replacer již existuje. Žádné změny nebyly provedeny.")
        return

    if 'app:' in content:
        # Máme app, ale chybí payload
        new_content = insert_payload_into_app(content)
        print("Vložil jsem payload do existující sekce app.")
    else:
        # Nemáme vůbec app
        new_content = insert_full_app_block(content)
        print("Vložil jsem novou sekci app/payload do defineNuxtConfig.")

    path.write_text(new_content, encoding='utf-8')
    print(f"Soubor '{path_str}' byl úspěšně aktualizován.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
