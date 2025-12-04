import json
import re
import os
import glob
from rdflib import Graph, URIRef, RDFS

# --- KONFIGURASJON ---
DATA_DIR = "data"
ONTOLOGY_FILE = os.path.join(DATA_DIR, "ontologi_kl06_20240523.ttl")
MD_SOURCE_FILE = os.path.join(DATA_DIR, "Grep_eksempelsamling_json.md")
OUTPUT_FILE = "python_sdk/models.py"

print("--- 🐍 GREP PYTHON SDK GENERATOR v11 (Strict Fix) 🐍 ---")

# 1. Last Ontologi
g = Graph()
try:
    g.parse(ONTOLOGY_FILE, format="turtle")
    print(f"✅ Ontologi lastet.")
except:
    print("⚠️  Ingen ontologi, kjører uten dok.")

# 2. Hjelpere
def pascal_case(s):
    if "/" in s: s = s.split("/")[-1]
    s = s.replace("_lk20", "-lk20") 
    return "".join(word.capitalize() for word in re.split(r'[-_]', s))

def get_doc(uri):
    if not uri: return ""
    target = uri.split('/')[-1].lower()
    for s, p, o in g.triples((None, RDFS.label, None)):
        if isinstance(s, URIRef) and s.split('/')[-1].lower() == target:
            for _, _, comment in g.triples((s, RDFS.comment, None)):
                if comment.language in ['nb', 'no', 'nob']: 
                    return comment.value.replace("\n", " ")
    return ""

def map_python_type(key, value):
    # SPESIALHANDLING: 'tittel' kan være både str, list og dict. 
    # Vi setter den til Any for å slippe valideringsfeil.
    if key == 'tittel': return "Any"
    
    # Normal mapping
    if isinstance(value, list): return "List[Any]" 
    if isinstance(value, dict): return "Dict[str, Any]" # <-- VIKTIG: Håndter objekter!
    if isinstance(value, bool): return "bool"
    if isinstance(value, (int, float)): return "float"
    
    return "str"

# 3. Scan Data (Hybrid/Golden)
class_registry = {} 
metadata_registry = {} 

def scan(data):
    if isinstance(data, dict):
        grep_type = data.get("grep-type")
        if grep_type:
            c_name = pascal_case(grep_type)
            if c_name not in class_registry:
                class_registry[c_name] = {}
                metadata_registry[c_name] = {"uri": grep_type, "doc": get_doc(grep_type)}
            
            for k, v in data.items():
                # Vi overskriver kun hvis feltet ikke finnes, ELLER hvis det var 'str' før og nå er noe annet
                if k not in class_registry[c_name]:
                    class_registry[c_name][k] = map_python_type(k, v)
        
        for v in data.values(): scan(v)
    elif isinstance(data, list):
        for i in data: scan(i)

# Les alt i data-mappen
files = glob.glob(os.path.join(DATA_DIR, "*.json"))
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        try: scan(json.load(file))
        except: pass

# 4. Generer Python-kode
os.makedirs("python_sdk", exist_ok=True)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("# AUTOGENERERT FIL\n")
    f.write("from pydantic import BaseModel, Field\n")
    f.write("from typing import List, Optional, Any, Dict\n\n") # <-- Lagt til Dict
    
    for c_name, props in sorted(class_registry.items()):
        meta = metadata_registry.get(c_name)
        
        f.write(f"class {c_name}(BaseModel):\n")
        f.write(f'    """\n    {meta["doc"]}\n    Se: {meta["uri"]}\n    """\n')
        
        for key, py_type in props.items():
            if "-" in key:
                safe_name = key.replace("-", "_")
                f.write(f'    {safe_name}: Optional[{py_type}] = Field(None, alias="{key}")\n')
            else:
                f.write(f'    {key}: Optional[{py_type}] = None\n')
        
        f.write("\n")

print(f"🎉 Ferdig! Genererte modeller i {OUTPUT_FILE}")