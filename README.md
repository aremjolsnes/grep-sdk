# @udir/grep-sdk 📚
## Developer SDK for Grep data from the Norwegian Directorate for Education and Training (Udir).

![Build Status](https://github.com/Utdanningsdirektoratet/grep-sdk/actions/workflows/release.yml/badge.svg)

`grep-sdk` removes the guesswork when integrating with the Norwegian Directorate for Education and Training's Grep database (LK20 and LK06). The library provides ready-made data models, automatic code documentation (IntelliSense), and type-safe communication with the API.

### Why use this? 🚀

Previously, you had to look up the [Grep Wiki](https://grepwiki.udir.no) to understand the field names in the JSON response. Now you get the answer right in your editor.

-   ✅ **Full Type Safety**: We know the difference between `Kompetansemaal` and `Kjerneelement` so you avoid runtime errors.
-   ✅ **Rich Documentation**: Definitions from the Grep ontology appear as help text when you hover over fields in the code.
-   ✅ **Universal Support**: Handles both the Knowledge Promotion (LK20) and the Knowledge Promotion Reform (LK06) with automatic fallback.

---

## 📦 Installation

### Node.js / TypeScript
```Bash
npm install @udir/grep-sdk
```

### Python
```Bash
pip install udir-grep
```

### .NET / C#
Add the project reference or install the package:
```Bash
dotnet add package Udir.GrepSdk
```
*(See [dotnet_sdk/README.md](dotnet_sdk/README.md) for details)*

### Java
repositories {
    maven { url = uri("https://maven.pkg.github.com/Utdanningsdirektoratet/grep-sdk") }
}

dependencies {
    implementation 'no.udir.grep:java_sdk:0.9.5'
}
*(See [java_sdk/README.md](java_sdk/README.md) for details)*

---

## 💻 Usage

### TypeScript (Node.js)
The client automatically checks if the code belongs to LK20 or LK06.
```TypeScript
import { GrepClient } from '@udir/grep-sdk';

const client = new GrepClient();

async function fetchPlan() {
  // Fetches Mathematics (LK20)
  const plan = await client.getLaereplan("MAT01-05");
  
  console.log(`Title: ${plan.tittel.nob}`);
  console.log(`Type: ${plan['grep-type']}`); // .../laereplan_lk20

  // Fallback: Fetches old RLE plan (LK06)
  const oldPlan = await client.getLaereplan("RLE1-02");
}
```

### Python
The SDK uses Pydantic for validation and type safety.
```Python
from udir_grep import GrepClient

client = GrepClient()

# Fetches Mathematics (LK20)
plan = client.get_laereplan("MAT01-05")

# Note: Field names with hyphens become underscores in Python
print(f"Title: {plan.tittel['nob']}")
print(f"Type: {plan.grep_type}")
```

### .NET / C#
```C#
using Udir.GrepSdk;

var client = new GrepClient();
var plan = await client.GetLaereplanAsync("MAT01-05");
```

### Java
```Java
GrepClient client = new GrepClient();
Object plan = client.getLaereplan("MAT01-05").get();
```

---

## Coverage
The SDK provides coverage of all 44 object types in Grep, including:
- Curricula (Læreplaner), Competence Aim Sets (Kompetansemålsett), and Competence Aims (Kompetansemål)
- Core Elements (Kjerneelementer) and Interdisciplinary Topics (Tverrfaglige temaer)
- Assessment Arrangements (Vurderingsordninger) and Exam Forms (Eksamensformer)
- Education Programmes (Utdanningsprogram) and Programme Areas (Programområder)
- Subject Codes (Fagkoder)

## License
MIT © Utdanningsdirektoratet