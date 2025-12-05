# Grep SDK for .NET

A .NET SDK for the Norwegian Directorate for Education and Training (Udir) Grep API.

## Installation

Install the package from NuGet:
```bash
dotnet add package Aremjolsnes.GrepSdk
```

## Usage

```csharp
using Aremjolsnes.GrepSdk;
using Aremjolsnes.GrepSdk.Models;

var client = new GrepClient();

// Fetch a curriculum (Læreplan)
// The SDK automatically handles fallback between LK20 and LK06 endpoints.
var result = await client.GetLaereplanAsync("MAT01-05");

if (result is LaereplanLk20 lk20)
{
    Console.WriteLine($"LK20 Plan: {lk20.Kode}");
}
else if (result is Laereplan lk06)
{
    Console.WriteLine($"LK06 Plan: {lk06.Kode}");
}
```

## Features

- **Automatic Fallback**: Tries `*-lk20` endpoints first, then falls back to legacy endpoints.
- **Typed Models**: Provides strong typing for Grep data structures, including:
  - `Laereplan` / `LaereplanLk20`
  - `Kompetansemaalsett` / `KompetansemaalsettLk20`
  - `Kompetansemaal` / `KompetansemaalLk20`
  - `Aarstrinn`
