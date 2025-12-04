# @udir/grep-sdk 📚
## Utviklerpakken for Grep-data fra Utdanningsdirektoratet.

grep-sdk fjerner gjettingen ved integrasjon mot Utdanningsdirektoratets Grep-database (LK20 og LK06). Biblioteket gir deg ferdige datamodeller, automatisk dokumentasjon i koden (IntelliSense) og typesikker kommunikasjon med API-et.
Hvorfor bruke denne? 🚀

Før måtte du slå opp i [Grep Wiki](https://grepwiki.udir.no) for å forstå feltnavnene i JSON-responsen. Nå får du svaret rett i editoren.
    ✅ Full Typesikkerhet: Vi vet forskjellen på Kompetansemaal og Kjerneelement slik at du slipper runtime-feil.
    ✅ Rik Dokumentasjon: Definisjoner fra Grep-ontologien vises som hjelpetekst når du holder musen over felter i koden.
    ✅ Universell Støtte: Håndterer både Fagfornyelsen (LK20) og Kunnskapsløftet (LK06) med automatisk fallback.

### 📦 Installasjon
#### Node.js / TypeScript
```Bash
npm install @udir/grep-sdk
```

#### Python
```Bash
pip install udir-grep
```

## 💻 Bruk
### TypeScript (Node.js)
Klienten sjekker automatisk om koden tilhører LK20 eller LK06.
```TypeScript
import { GrepClient } from '@udir/grep-sdk';

const client = new GrepClient();

async function hentPlan() {
  // Henter Matematikk (LK20)
  const plan = await client.getLaereplan("MAT01-05");
  
  console.log(`Tittel: ${plan.tittel.nob}`);
  console.log(`Type: ${plan['grep-type']}`); // .../laereplan_lk20

  // Fallback: Henter gammel RLE-plan (LK06)
  const gammelPlan = await client.getLaereplan("RLE1-02");
}

```

### Python
SDK-en bruker Pydantic for validering og typesikring.
```Python
from udir_grep import GrepClient

client = GrepClient()

# Henter Matematikk (LK20)
plan = client.get_laereplan("MAT01-05")

# Merk: Feltnavn med bindestrek blir underscore i Python
print(f"Tittel: {plan.tittel['nob']}")
print(f"Type: {plan.grep_type}")

```
## Dekning
SDK-en gir dekning av alle 44 objekttyper i Grep, inkludert:
- Læreplaner, Kompetansemålsett og Kompetansemål
- Kjerneelementer og Tverrfaglige temaer
- Vurderingsordninger og Eksamensformer
- Utdanningsprogram og Programområder
- Fagkoder

## Lisens
MIT © Utdanningsdirektoratet