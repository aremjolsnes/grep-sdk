# Grep SDK for Java

A Java SDK for the Norwegian Directorate for Education and Training (Udir) Grep API.

## Installation

Add the dependency to your `build.gradle`:

```groovy
repositories {
    mavenCentral()
    maven { url = uri("https://maven.pkg.github.com/aremjolsnes/grep-sdk") }
}

dependencies {
    implementation 'com.github.aremjolsnes:java_sdk:0.9.10'
    implementation 'com.fasterxml.jackson.core:jackson-databind:2.15.2'
    implementation 'com.squareup.okhttp3:okhttp:4.12.0'
}
```

## Usage

```java
import com.github.aremjolsnes.GrepClient;
import com.github.aremjolsnes.models.LaereplanLk20;
import com.github.aremjolsnes.models.Laereplan;

public class Main {
    public static void main(String[] args) throws Exception {
        GrepClient client = new GrepClient();

        // Fetch a curriculum (Læreplan)
        // Returns a CompletableFuture
        Object result = client.getLaereplan("MAT01-05").get();

        if (result instanceof LaereplanLk20) {
            LaereplanLk20 lk20 = (LaereplanLk20) result;
            System.out.println("LK20 Plan: " + lk20.kode);
        } else if (result instanceof Laereplan) {
            Laereplan lk06 = (Laereplan) result;
            System.out.println("LK06 Plan: " + lk06.kode);
        }
    }
}
```

## Features

- **Automatic Fallback**: Tries `*-lk20` endpoints first, then falls back to legacy endpoints.
- **Typed Models**: Provides strong typing for Grep data structures, including:
  - `Laereplan` / `LaereplanLk20`
  - `Kompetansemaalsett` / `KompetansemaalsettLk20`
  - `Kompetansemaal` / `KompetansemaalLk20`
  - `Aarstrinn`
- **Async Support**: Uses `CompletableFuture` for non-blocking I/O.
