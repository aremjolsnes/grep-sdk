import json
import re
import os
import glob
import csv
from rdflib import Graph, URIRef, RDFS

# --- KONFIGURASJON ---
DATA_DIR = "data"
ONTOLOGY_FILE = os.path.join(DATA_DIR, "ontologi_kl06_20240523.ttl")
MD_SOURCE_FILE = os.path.join(DATA_DIR, "Grep_eksempelsamling_json.md")
OUTPUT_FILE = "src/types.ts"

print("--- 🏭 GREP SDK GENERATOR v10 (Golden Sample Edition) 🏭 ---")

# 1. Last Ontologi 🧠
print(f"⏳ Laster ontologi fra {ONTOLOGY_FILE}...")
g = Graph()
try:
    g.parse(ONTOLOGY_FILE, format="turtle")
    print(f"✅ Ontologi lastet ({len(g)} tripler).")
except Exception as e:
    print(f"❌ Kunne ikke laste ontologi: {e}")

# 2. Hjelpefunksjoner 🛠️
def pascal_case(s):
    if "/" in s: s = s.split("/")[-1]
    s = s.replace("_lk20", "-lk20") 
    return "".join(word.capitalize() for word in re.split(r'[-_]', s))

def get_class_info(term_uri_string):
    if not term_uri_string: return None
    target_local_name = term_uri_string.split('/')[-1].lower()
    for s, p, o in g.triples((None, RDFS.label, None)):
        if isinstance(s, URIRef) and s.split('/')[-1].lower() == target_local_name:
            c_no, c_en = "", ""
            for _, _, comment in g.triples((s, RDFS.comment, None)):
                if comment.language in ['nb', 'no', 'nob']: c_no = comment.value
                elif comment.language in ['en', 'eng']: c_en = comment.value
            return {"name": s.split('/')[-1], "desc_no": c_no, "desc_en": c_en, "uri": str(s)}
    return None

def map_json_type(value):
    """Mapper JSON-verdier til TypeScript-typer."""
    if isinstance(value, dict):
        # Hvis det er et objekt (f.eks 'kompetansemaal-overskrift'), men ikke en Grep-type
        # kan vi kalle det 'any' eller 'object' for nå. 
        return "any" 
    if isinstance(value, list): return "any[]" 
    if isinstance(value, bool): return "boolean"
    if isinstance(value, (int, float)): return "number"
    return "string"

# 3. Registere 📚
class_registry = {} 
metadata_registry = {} 

# --- REKURSIV SCANNER (Motoren) ---
def scan_object_recursive(data, source_name=""):
    if isinstance(data, dict):
        grep_type_uri = data.get("grep-type")
        if grep_type_uri:
            class_name = pascal_case(grep_type_uri)
            
            # Opprett type hvis ny
            if class_name not in class_registry:
                class_registry[class_name] = {}
                metadata_registry[class_name] = get_class_info(grep_type_uri)
            
            # Legg til alle felter fra dette eksemplet
            for key, value in data.items():
                if key not in class_registry[class_name]:
                    class_registry[class_name][key] = map_json_type(value)

        # Fortsett dybdescan uansett om det var en grep-type eller ikke
        for value in data.values():
            scan_object_recursive(value, source_name)     
            
    elif isinstance(data, list):
        for item in data:
            scan_object_recursive(item, source_name)

# 4. Kjør prosessering 🚀

# A. Markdown
if os.path.exists(MD_SOURCE_FILE):
    print(f"⏳ Scanner Markdown...")
    with open(MD_SOURCE_FILE, "r", encoding="utf-8") as f:
        blocks = re.findall(r'```(?:\w+)?(.*?)```', f.read(), re.DOTALL)
        for b in blocks:
            try: scan_object_recursive(json.loads(b), "markdown")
            except: pass

# B. Løse JSON-filer (HER KOMMER GULLET!)
loose_json = glob.glob(os.path.join(DATA_DIR, "*.json"))
print(f"⏳ Scanner {len(loose_json)} JSON-filer (inkludert Golden Samples)...")
for file_path in loose_json:
    print(f"   -> Leser {os.path.basename(file_path)}")
    with open(file_path, "r", encoding="utf-8") as f:
        try: scan_object_recursive(json.loads(f.read()), file_path)
        except Exception as e: 
            print(f"⚠️ Feil i {file_path}: {e}")

# 5. Skriv til fil 💾
os.makedirs("src", exist_ok=True)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("// AUTOGENERERT FIL\n")
    f.write("// Bygget på faktiske API-responser (Golden Samples)\n\n")
    
    for class_name, props in sorted(class_registry.items()):
        class_info = metadata_registry.get(class_name)
        
        f.write("/**\n")
        if class_info:
            f.write(f" * {class_info.get('desc_no', '')}\n")
            f.write(f" * @see {class_info['uri']}\n")
        f.write(" */\n")
        
        f.write(f"export interface {class_name} {{\n")
        
        for key, ts_type in props.items():
            safe_key = f"'{key}'" if "-" in key else key
            
            # Gjør felter optional (?) hvis vi mistenker at de ikke alltid er der,
            # men siden vi bruker "Golden Samples" med "alle properties", kan vi være strengere.
            # Vi kjører safe med optional for å unngå runtime crashes.
            f.write(f"  {safe_key}?: {ts_type};\n")
            
        f.write("}\n\n")

print(f"🎉 Suksess! Oppdatert {OUTPUT_FILE}")

# Verifisering
found_lk06 = "Kompetansemaalsett" in class_registry
found_lk20 = "KompetansemaalsettLk20" in class_registry

if found_lk06 and found_lk20:
    print("✅ BEKREFTET: Fant både LK06 og LK20 kompetansemålsett!")
else:
    print(f"⚠️ Status: LK06={found_lk06}, LK20={found_lk20}")