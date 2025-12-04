> Se artikkelen https://github.com/Utdanningsdirektoratet/KL06-LK20-public/wiki/om-vurderingsordning-i-REST-og-RDF[Om vurderingsordning i REST og RDF] i REST-wikiwn vår for å se hvordan dette er løst i hhv. REST og RDF for fagkoder.


> Vi har også skrevet litt om fravær av forflatning og oppløfting av attributter for "vurderingsordningser-kapittelet" i læreplanen (LK20). Se: https://github.com/Utdanningsdirektoratet/Grep_SPARQL/wiki/vurderingsordninger-kapittel["vurderingsordninger-kapittel"] som handler om hvordan vi kan takle flere lag av blanke noder når objekter ikke er forflatet og løftet opp slik det er beskrevet nedenfor.

Som kjent er .json default-formatet for REST-kall mot Grep. Dette formatet gir en hierarkisk struktur som du kan traversere gjennom når du bruker dataene til å skape noe med f.eks. javascript.

Da vi skulle gjenskape disse dataene i et RDF SPARQL-endepunkt (triple store), måtte vi ha i mente at måten å lagre data på i denne sammenhengen i prinsippet er som å lage en tabell med tre kolonner: *subjekt*, *predikat* (eller property) og *objekt* (eller verdi/value) - eller uttrykt med SPARQL: 
[quote]
*?s*, *?p*, *?o* .

Dataene lagres da gjennom en rekke statements (påstander/erklæringer) av typen 
[quote]
d:NOR01-06 rdf:type u:laereplan_lk20 .

(altså at NOR01-06 er av typen 'laereplan_lk20', og f.eks d:NOR01-06 u:tittel "Læreplan i norsk" osv., som vist i tabellen nedenfor:

.triple store
|===
|?s |?p |?o

|d:NOR01-06
|rdf:type
|u:laereplan_lk20

|d:NOR01-06
|u:tittel
|"Læreplan i norsk"
|===

("u:" og "d:" i eksemplene er såkalte prefikser som du kan lese mer om på siden link:../Prefikser[Prefikser].

For å enklere få overført dataene fra Grep til vår "triple store" måtte vi derfor konvertere dataene til en flatere struktur. Vi har valgt å gjøre det via formatet JSON-LD. JSON-LD er i prinsippet det samme som vanlig JSON, med unntak av starten av innholdet i .jsonld-fila som bringer inn elementet @context - som gjør det til en Linked Data-fil (derfor LD i JSON-LD). Mer om @context på https://w3c.github.io/json-ld-syntax/#the-context.

Videre har vi laget en automatisk rutine som "løfter" og "forflater" den hierarkiske dokumentstrukturen i JSON, slik at outputen til JSON-LD, og videre importen til trippel-databasen, blir så "flat" og "datasentrisk" som mulig. De som er kjent med RDF og SPARQL vil da forstå at dette vil gjøre at vi unngår en masse såkalte "blanke noder" (blanke noder er vanskelig å søke i). Vi beskriver ikke dette nærmere her, men nøyer oss med å si at det finnes en god del dokumentasjon på nettet om både RDF, SPARQL og blanke noder ("blank nodes" på engelsk). Vi har i hvert fall prøvd å unngå dem så godt vi har kunnet, med unntak av "gyldig-fra" og "gyldig-til" på referanseobjekter. Der gir de blanke nodene en verdi. Vi har en egen artikkel om https://github.com/Utdanningsdirektoratet/Grep_SPARQL/wiki/Blanke-noder-for-gyldighetsinformasjon-i-referanseobjekter[Blanke noder for gyldighetsinformasjon i referanseobjekter] der vi går mer i dybden på dette.


### Eksempel på "løfting":
Hvis noe ser slik ut i .json
[source,json]
----
"fastsettelsesinformasjon": {
   "fastsatt-dato": "2019-11-15T00:00:00",
   }
----
endres det til dette i .jsonld
[source,jsonld]
----
"fastsatt-dato": "2019-11-15T00:00:00",
----
Her løftes altså "fastsatt-dato" opp fra å være et objekt for "fastsettelsesinformasjon", til å være en egen egenskap for (i dette tilfellet) den aktuelle læreplanen.

### Eksempel på "forflating":
Hvis noe ser slik ut i .json
[source,json]
----
"fastsatt-spraak": {
"kode": "nob",
"uri": "http://psi.udir.no/kl06/nob",
"url-data": "https://data.udir.no/kl06/v201906/spraak/nob",
"tittel": "Bokmål",
"gyldighet": {
"gyldig-fra": null,
"gyldig-til": null
},
----
endres det til dette i .jsonld
[source,jsonld]
----
"fastsatt-spraak": {
  "uriId": "http://psi.udir.no/kl06/nob"
----
Dataene er uansett lagret i objektet "http://psi.udir.no/kl06/nob", og trenger ikke gjentas her i denne (som i eksempelet) læreplanen. Det eneste vi trenger, er referansen til http://psi.udir.no/kl06/nob.



I tabellen nedenfor har vi prøvd å beskrive dette fullt ut for en læreplan. Her har vi også tatt med en kolonne "Type" som blant annet angir hvilken datatype du kan forvente å finne i verdier for disse egenskapene (klikk for å åpne tabellen).

.Åpne tabell 2: Læreplan (LK20)
[%collapsible]
====
[cols="1,1,2", options="header"] 
.Læreplan (LK20)
|===
|JSON
|JSON-LD
|Type

|id
|id
|String

|kode
|kode
|String

|uri
|uri 
|String (url i sparql)

|url-data
|url-data
|String (url i sparql)

|tittel
|-
|-

|tittel.spraak
|-
|-

|tittel.verdi
|tittel [*]
|Array av språkversjonert tekst

|kortform
|-
|-

|kortform.spraak
|-
|-


|kortform.verdi
|kortform[*]
|Array av språkversjonert tekst

|grep-type
|grep-type
|String (url i sparql)

|status
|status
|String (url i sparql)

|sist-endret
|sist-endret
|String (url i sparql)

|sist-endret
|sist-endret
|DATETIME ('YYYY-MM-DD hh:mm:ss.fraction')

|fastsettelsesinformasjon
|-
|-

|fastsettelsesinformasjon.fastsatt-dato
|fastsatt-dato
|DATETIME ('YYYY-MM-DD hh:mm:ss.fraction')

|fastsettelsesinformasjon.fastsettelsestekst.spraak
|-
|-

|fastsettelsesinformasjon.fastsettelsestekst.verdi
|fastsettelsestekst [*]
|Array av språkversjonert tekst

|fastsettelsesinformasjon.fastsatt-spraak
|-
|-

|fastsettelsesinformasjon.fastsatt-spraak.kode
|-
|-

|fastsettelsesinformasjon.fastsatt-spraak.uri
|fastsatt-spraak
|uri-referanse (eksempel: 'http://psi.udir.no/kl06/nob')

|fastsettelsesinformasjon.fastsatt-spraak.url-data
|-
|-

|fastsettelsesinformasjon.fastsatt-spraak.url-data
|-
|-

|fastsettelsesinformasjon.fastsatt-spraak.id
|-
|-

|fastsettelsesinformasjon.fastsatt-spraak.grep-type
|-
|-

|fastsettelsesinformasjon.fastsatt-spraak.status
|-
|-

|fastsatt-dato-overskrift
|-
|-

|fagtype
|-
|-

|fagtype.kode
|-
|-


|fagtype.uri
|fagtype [*]
|Array av uri-referanser

|fagtype.url-data
|-
|-

|fagtype.tittel
|-
|-

|fagtype.gyldighet {...}
|-
|-

|fagtype.id
|-
|-

|fagtype.grep-type
|-
|-

|fagtype.status
|-
|-

|tilgjengelige-spraak
|-
|-

|tilgjengelige-spraak.kode
|-
|

|tilgjengelige-spraak.uri
|tilgjengelige-spraak[*]
|Array av uri-referanser

|tilgjengelige-spraak.url-data
|-
|-

|tilgjengelige-spraak.tittel
|-
|-

|tilgjengelige-spraak.gyldighet {...}
|-
|-

|tilgjengelige-spraak.id
|-
|-

|tilgjengelige-spraak.grep-type
|-
|-

|tilgjengelige-spraak.status
|-
|-

|opplaeringsnivaa
|-
|-

|opplaeringsnivaa.kode
|-
|-

|opplaeringsnivaa.uri
| [*]
|Array av uri-referanser

|opplaeringsnivaa.url-data
|-
|-

|opplaeringsnivaa.tittel
|-
|-

|opplaeringsnivaa.gyldighet {...}
|-
|-

|opplaeringsnivaa.id
|-
|-

|opplaeringsnivaa.grep-type
|-
|-

|opplaeringsnivaa.status
|-
|-

|gyldighetsperiode
|-
|-

|gyldighetsperiode.gyldig-fra
|-
|-

|gyldighetsperiode.gyldig-fra.overskrift
|-
|-

|gyldighetsperiode.gyldig-fra.dato
|gyldig-fra
|DATETIME ('YYYY-MM-DD hh:mm:ss.fraction')

|gyldighetsperiode.gyldig-til
|-
|-

|gyldighetsperiode.gyldig-til.overskrift
|-
|-

|gyldighetsperiode.gyldig-til.dato
|gyldig-fra
|DATETIME ('YYYY-MM-DD hh:mm:ss.fraction')

|erstatter
|-
|-

|erstatter.kode
|-
|-

|erstatter.uri
| [*]
|Array av uri-referanser

|erstatter.url-data
|-
|-

|erstatter.tittel
|-
|-

|erstatter.gyldighet {...}
|-
|-

|erstatter.id
|-
|-

|erstatter.grep-type
|
|

|erstatter.status
|-
|-

|erstattes-av
|-
|-

|erstattes-av.kode
|-
|-

|erstattes-av.uri
| [*]
|Array av uri-referanser

|erstattes-av.url-data
|-
|-

|erstattes-av.tittel
|-
|-

|erstattes-av.gyldighet {...}
|-
|-

|erstattes-av.id
|-
|-

|erstattes-av.grep-type
|
|

|erstattes-av.status
|-
|-

|siste-eksamen
|siste-eksamen
|DATETIME ('YYYY-MM-DD hh:mm:ss.fraction')

|merkelapper
|-
|-

|merkelapper.kode
|-
|-

|merkelapper.uri
| [*]
|Array av uri-referanser

|merkelapper.url-data
|-
|-

|merkelapper.tittel
|-
|-

|merkelapper.gyldighet {...}
|-
|-

|merkelapper.id
|-
|-

|merkelapper.grep-type
|
|

|merkelapper.status
|-
|-

|om-faget-kapittel
|-
|-

|om-faget-kapittel.overskrift {...}
|-
|-

|om-faget-kapittel.fagets-relevans-og-verdier
|-
|-

|om-faget-kapittel.fagets-relevans-og-verdier-overskrift {...}
|-
|-

|om-faget-kapittel.forskrift
|-
|-

|om-faget-kapittel.forskrift
|-
|-

|om-faget-kapittel.fagets-relevans
|-
|-

|om-faget-kapittel.fagets-relevans.beskrivelse
|-
|-

|om-faget-kapittel.fagets-relevans.beskrivelse.tekst
|fagets-relevans [*]
|Array av språkversjonert tekst

|om-faget-kapittel.fagets-relevans.forklaring []
|-
|-

|om-faget-kapittel.fagets-relevans.beskrivelse.forskrift
|-
|-

|om-faget-kapittel.verdier-og-prinsipper
|-
|-

|om-faget-kapittel.verdier-og-prinsipper.beskrivelse
|-
|-

|om-faget-kapittel.verdier-og-prinsipper.beskrivelse.tekst
|fagets-relevans [*]
|Array av språkversjonert tekst

|om-faget-kapittel.verdier-og-prinsipper.forklaring []
|-
|-

|om-faget-kapittel.verdier-og-prinsipper.beskrivelse.forskrift
|-
|-

|om-faget-kapittel.kjerneelementer-i-faget
|-
|-

|om-faget-kapittel.kjerneelementer-i-faget.overskrift {...}
|-
|-

|om-faget-kapittel.kjerneelementer-i-faget.kjerneelementer []
|kjerneelementer [*]
|Array av uri-referanser

|om-faget-kapittel.tverrfaglige-temaer-i-faget
|-
|-

|om-faget-kapittel.tverrfaglige-temaer-i-faget.overskrift {...}
|-
|-

|om-faget-kapittel.tverrfaglige-temaer-i-faget.kjerneelementer []
|kjerneelementer [*]
|Array av uri-referanser

|om-faget-kapittel.grunnleggende-ferdigheter-i-faget
|-
|-

|om-faget-kapittel.grunnleggende-ferdigheter-i-faget.overskrift {...}
|-
|-

|om-faget-kapittel.grunnleggende-ferdigheter-i-faget.kjerneelementer []
|kjerneelementer [*]
|Array av uri-referanser

|kompetansemaal-kapittel
|-
|-

|kompetansemaal-kapittel.overskrift {...}
|-
|-

|kompetansemaal-kapittel.forkrift
|-
|-

|kompetansemaal-kapittel.kompetansemaalsett [
|-
|-

|kompetansemaal-kapittel.kompetansemaalsett.kode
|-
|-

|kompetansemaal-kapittel.kompetansemaalsett.uri
| [*]
|Array av uri-referanser

|kompetansemaal-kapittel.kompetansemaalsett.url-data
|-
|-

|kompetansemaal-kapittel.kompetansemaalsett.tittel
|-
|-

|kompetansemaal-kapittel.kompetansemaalsett.gyldighet
|-
|-

|kompetansemaal-kapittel.kompetansemaalsett.id
|-
|-

|kompetansemaal-kapittel.kompetansemaalsett.grep-type
|-
|-

|kompetansemaal-kapittel.kompetansemaalsett.status ]
|-
|-

|vurderingsordning-kapittel
|-
|-

|vurderingsordning-kapittel.overskrift {...}
|-
|-

|vurderingsordning-kapittel.forskrift
|-
|-

|vurderingsordning-kapittel.beskrivelse
|-
|-

|vurderingsordning-kapittel.beskrivelse.tekst
|-
|-

|vurderingsordning-kapittel.beskrivelse.tekst.spraak
|-
|-

|vurderingsordning-kapittel.beskrivelse.tekst.verdi
|vurderingsordning  [*]
|Array av språkversjonert tekst

|vurderingsordning-kapittel.forklaring
|-
|-

|tilleggsopplysninger
|tilleggsopplysninger
|String

|===
====

Har du forslag til forbedring av denne beskrivelsen, er det bare å ta kontakt med oss, evt. opprette en "issue" her i Github