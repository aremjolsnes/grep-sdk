import json
import re
import os

# Konfigurasjon
LOL_FILE = "data/lol.json"
TYPES_FILE = "src/types.ts"

print("--- 🕵️ GREP SDK DEKNINGSANALYSE ---")

# 1. Hent fasiten fra lol.json (Alle gyldige Grep-typer)
if not os.path.exists(LOL_FILE):
    print(f"❌ Finner ikke {LOL_FILE}. Legg den i data-mappen!")
    exit()

with open(LOL_FILE, "r", encoding="utf-8") as f:
    lol_data = json.load(f)

# Hent ut alle "grep-type" URI-er fra fasiten
expected_types = set()
for item in lol_data:
    if "grep-type" in item:
        expected_types.add(item["grep-type"])

print(f"Stats fra lol.json (Fasit): Forventer {len(expected_types)} unike typer.")

# 2. Hjelpefunksjon for å gjette ClassName fra URI (samme logikk som builder.py)
def uri_to_classname(uri):
    if "/" in uri: uri = uri.split("/")[-1]
    uri = uri.replace("_lk20", "-lk20")
    return "".join(word.capitalize() for word in re.split(r'[-_]', uri))

# Bygg et sett med forventede klassenavn
expected_classnames = {uri_to_classname(uri) for uri in expected_types}

# 3. Les hva vi faktisk har generert i types.ts
if not os.path.exists(TYPES_FILE):
    print(f"❌ Finner ikke {TYPES_FILE}. Kjør builder.py først!")
    exit()

with open(TYPES_FILE, "r", encoding="utf-8") as f:
    ts_content = f.read()

# Finn alle "export interface X"
generated_interfaces = set(re.findall(r'export interface (\w+)', ts_content))

print(f"Stats fra types.ts (Resultat): Fant {len(generated_interfaces)} genererte interfaces.")

# 4. Sammenlign! ⚖️
missing = expected_classnames - generated_interfaces
extras = generated_interfaces - expected_classnames

print("\n--- RESULTAT ---")

if len(missing) == 0:
    print("✅ GRATULERER! 100% DEKNING AV ALLE TYPER I LOL.JSON!")
else:
    print(f"⚠️  Mangler {len(missing)} typer:")
    for m in sorted(missing):
        print(f"   - {m}")

if len(extras) > 0:
    print(f"\nℹ️  (Vi genererte også {len(extras)} ekstra hjelpetyper som ikke står i lol.json, f.eks. lister):")
    # Vi lister bare opp de første for ikke å spamme
    print(f"   - {', '.join(list(extras)[:5])}...")

print("\n----------------")