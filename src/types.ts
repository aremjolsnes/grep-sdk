// AUTOGENERERT FIL
// Bygget på faktiske API-responser (Golden Samples)

/**
 * Utdanningsnivå som angir progresjon for det 13-årige utdanningsløpet
 * @see http://psi.udir.no/ontologi/kl06/Aarstrinn
 */
export interface Aarstrinn {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  'numerisk-verdi'?: number;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
  gyldighet?: any;
  label?: any[];
}

/**
 * Property for notice ("merknad") to specify whether it applies to either "diploma" or "certificate of competence/vocational training certificate"
 * @see http://psi.udir.no/ontologi/kl06/dokumenttype
 */
export interface Dokumenttype {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  beskrivelse?: any[];
  kortform?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
  label?: any[];
}

/**
 * Element for å angi hvilken eksamensform som skal påføres vitnemålet
 * @see http://psi.udir.no/ontologi/kl06/Eksamensform
 */
export interface Eksamensform {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
  gyldighet?: any;
  label?: any[];
}

/**
 * Element for å angi hva slags eksamensordning som gjelder for elever og privatister
 * @see http://psi.udir.no/ontologi/kl06/Eksamensordning
 */
export interface Eksamensordning {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
  gyldighet?: any;
  label?: any[];
}

/**
 * Egenskap for fagområde for å angi hierarkisk overordnet faglig innholdskategori (for statistisk bruk)
 * @see http://psi.udir.no/ontologi/kl06/fagkategori
 */
export interface Fagkategori {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  gyldighet?: any;
  label?: any[];
}

/**
 * Element som fungerer som identifikator for et fag eller del av et fag, for presist å kunne angi opplæring, eksamensgjennomføring, vurdering og dokumentasjon, for eksempel MAT0011 "Matematikk 10.årstrinn, muntlig"
 * @see http://psi.udir.no/ontologi/kl06/Fagkode
 */
export interface Fagkode {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  merkelapper?: any[];
  vurderingsordning?: any[];
  opplaeringsfag?: any[];
  'tilleggseksamen-ikke-normalt-loep'?: any[];
  'benyttes-sammen-med'?: any[];
  spraaknivaa?: string;
  erstatter?: any[];
  'erstattes-av'?: any[];
  'omfang-totalt'?: string;
  'omfang-vitnemaal'?: string;
  'omfang-til-naa'?: string;
  'naar-kan-man-ta-eksamen'?: any;
  'naar-gis-det-undervisning'?: any;
  sensur?: any;
  oppgave?: any;
  tilleggsopplysninger?: any[];
  'bygger-paa-fag'?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  'iso-639-2-kode'?: string;
  fagtype?: any;
  opplaeringsnivaa?: any;
  kortform?: any[];
  gyldighet?: any;
  label?: any[];
}

/**
 * Gruppering av opplæringsfag i faglige innholdskategorier under fagketegorier (se fagkategori) for statistisk bruk
 * @see http://psi.udir.no/ontologi/kl06/Fagomraade
 */
export interface Fagomraade {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  fagkategori?: any[];
  label?: any[];
  gyldighet?: any;
}

/**
 * Gruppering av fag etter Rundskriv Udir-1-[et gitt årstall]
 * @see http://psi.udir.no/ontologi/kl06/fagtype
 */
export interface Fagtype {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  opplaeringsnivaa?: any;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
  label?: any[];
}

/**
 * Den delmengden av den totale kompetansen i fag som handler å vise de fem utvalgte ferdighetene: Å kunne lese, å kunne skrive, å kunne regne, muntlige og digitale ferdiheter
 * @see http://psi.udir.no/ontologi/kl06/Grunnleggende_ferdighet_lk20
 */
export interface GrunnleggendeFerdighetLk20 {
  'lenke-til-beskrivelse'?: string;
  rekkefoelge?: number;
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  gyldighet?: any;
  label?: any[];
}

/**
 * Delmengde av læreplan for inndeling av det faglige innholdet i logiske blokker
 * @see http://psi.udir.no/ontologi/kl06/Hovedomraade
 */
export interface Hovedomraade {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  beskrivelse?: any[];
  'underliggende-hovedomraader'?: any[];
  rekkefoelge?: number;
  gyldighet?: any;
  status?: string;
  label?: any[];
}

/**
 * Grep-type som brukes av andre systemer som autoritetsregister til å angi lovlige karakteruttrykk i dokumentasjon (vitnemål o.l), f.eks. "BESTÅTT", "FEM", "IKKE BESTÅTT"
 * @see http://psi.udir.no/ontologi/kl06/Karakter
 */
export interface Karakter {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
  label?: any[];
  gyldighet?: any;
}

/**
 * Element som sammen med de andre i samme læreplan, uttrykker hva som er det viktigste i faget og hva elevene/lærlingene/praksiskandidatene må lære for å mestre og bruke faget (kan være kunnskapsområder, metoder, begreper, tenkemåter og uttrykksformer)
 * @see http://psi.udir.no/ontologi/kl06/Kjerneelement_lk20
 */
export interface KjerneelementLk20 {
  rekkefoelge?: number;
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any;
  beskrivelse?: any;
  'grep-type'?: string;
  forklaring?: any[];
  status?: string;
  'sist-endret'?: string;
  'tilhoerer-laereplan'?: any;
  gyldighet?: any;
  label?: any[];
}

/**
 * Element (for læreplaner i LK06) som angir en delmengde av den kompetanse en elev/lærling/praksiskandidat skal ha oppnådd etter endt opplæring på et gitt nivå/trinn
 * @see http://psi.udir.no/ontologi/kl06/Kompetansemaal
 */
export interface Kompetansemaal {
  rekkefoelge?: number;
  'tilhoerer-hovedomraade'?: any;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  'laereplan-referanser'?: any[];
  label?: any[];
}

/**
 * Element (for læreplaner i LK20) som angir en delmengde av den kompetanse en elev/lærling/praksiskandidat/deltaker skal ha oppnådd etter endt opplæring på et gitt nivå/trinn
 * @see http://psi.udir.no/ontologi/kl06/Kompetansemaal_lk20
 */
export interface KompetansemaalLk20 {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  rekkefoelge?: number;
  'tilknyttede-tverrfaglige-temaer'?: any[];
  'tilknyttede-kjerneelementer'?: any[];
  'tilknyttede-grunnleggende-ferdigheter'?: any[];
  'tilknyttede-verb'?: any[];
  'bygger-paa'?: any[];
  'samme-som'?: any[];
  'tilhoerer-kompetansemaalsett'?: any;
  'tilhoerer-laereplan'?: any;
  'gjenbruk-av'?: string;
  'hentet-fra'?: any;
  forklaring?: any[];
  'sist-endret'?: string;
  label?: any[];
}

/**
 * Egenskap for 'Laereplan' og 'Laereplan_lk20' for å angi hvilke competence aim set den består av
 * @see http://psi.udir.no/ontologi/kl06/kompetansemaalsett
 */
export interface Kompetansemaalsett {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  'etter-fag'?: any[];
  programfag?: any;
  'hovedomraader-i-kontekst-av-kompetansemaalsett'?: any[];
  kompetansemaal?: any[];
  'tilhoerer-laereplan'?: any;
  'maal-for-kompetansemaalene-overskrift'?: any[];
  'benyttes-paa-aarstrinn'?: any[];
  'etter-aarstrinn'?: any[];
  gyldighet?: any;
  status?: string;
  rekkefoelge?: number;
  label?: any[];
}

/**
 * Et sett med kompetansemål som gjelder for et spesifisert sett med trinn eller nivåer
 * @see http://psi.udir.no/ontologi/kl06/Kompetansemaalsett_lk20
 */
export interface KompetansemaalsettLk20 {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any;
  kortform?: any[];
  'grep-type'?: string;
  rekkefoelge?: number;
  forklaring?: any[];
  status?: string;
  'sist-endret'?: string;
  'kompetansemaal-overskrift'?: any;
  'kompetansemaal-ingress'?: any;
  kompetansemaal?: any[];
  underveisvurdering?: any;
  standpunktvurdering?: any;
  'etter-fag'?: any[];
  'etter-aarstrinn'?: any[];
  'benyttes-paa-aarstrinn'?: any[];
  'tilhoerer-laereplan'?: any;
  gyldighet?: any;
  label?: any[];
}

/**
 * Element som uttrykker den samlede kompetansen en elev, lærling eller lærekandidat skal ha etter endt opplæring på et gitt nivå/trinn i ett eller flere fag etter Kunnskapsløftet LK06)
 * @see http://psi.udir.no/ontologi/kl06/Laereplan
 */
export interface Laereplan {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  'tilhoerende-kompetansemaalsett'?: any[];
  'sist-endret'?: string;
  merkelapper?: any[];
  'programfag-kapittel'?: any;
  'hovedomraade-kapittel'?: string;
  'kompetansemaal-kapittel'?: any;
  fastsettelsesinformasjon?: any;
  fagtype?: any[];
  'tilgjengelige-spraak'?: any[];
  opplaeringsnivaa?: any[];
  gyldighetsperiode?: any;
  erstatter?: any[];
  'erstattes-av'?: any[];
  'formaal-kapittel'?: any;
  'timetall-kapittel'?: any;
  'struktur-kapittel'?: any;
  'grunnleggende-ferdigheter-kapittel'?: any;
  'vurdering-kapittel'?: any;
  'siste-eksamen'?: string;
  'soekehjelp-navn-motsatt-maalform'?: string;
  tilleggsopplysninger?: string;
  label?: any[];
}

/**
 * Element som uttrykker den samlede kompetansen en elev, lærling,  lærekandidat eller deltaker skal ha etter endt opplæring på et gitt nivå/trinn i ett eller flere fag etter Kunnskapsløftet LK20, fagfornyelsen
 * @see http://psi.udir.no/ontologi/kl06/Laereplan_lk20
 */
export interface LaereplanLk20 {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  kortform?: any[];
  'sist-endret'?: string;
  laereplanstruktur?: any;
  fastsettelsesinformasjon?: any;
  fagtype?: any[];
  'tilgjengelige-spraak'?: any[];
  opplaeringsnivaa?: any[];
  ordforklaringer?: any[];
  gyldighetsperiode?: any;
  erstatter?: any[];
  'erstattes-av'?: any[];
  'siste-eksamen'?: string;
  merkelapper?: any[];
  'om-faget-kapittel'?: any;
  'kompetansemaal-kapittel'?: any;
  'vurderingsordning-kapittel'?: any;
  'vurderingsordninger-kapittel'?: any;
  tilleggsopplysninger?: any[];
  'opprinnelige-planer'?: any[];
  label?: any[];
  'tilhoerende-kompetansemaalsett'?: any[];
}

/**
 * Egenskap for læreplan (lk20) for å angi om hvilken struktur den følger (foreløpig) enten "vanlig" (strukturert etter årstrinn/fag) eller "modulstrukturert" (strukturert etter angitte moduler)
 * @see http://psi.udir.no/ontologi/kl06/Laereplanstruktur
 */
export interface Laereplanstruktur {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
  gyldighet?: any;
  label?: any[];
}

/**
 * Element for "programomraade" for å angi hvilken løpstype det er (p.t. er kun kryssløp tilgjengelig). Se også egenskapen "loepstype-kryssloep"
 * @see http://psi.udir.no/ontologi/kl06/Loepstype
 */
export interface Loepstype {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  beskrivelse?: any[];
  kortform?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
  label?: any[];
}

/**
 * Element for å angi spesifikke egenskaper for forekomster av fagkode, laereplan,  laereplan_lk20, opplaeringsfag og programomraade
 * @see http://psi.udir.no/ontologi/kl06/Merkelapp
 */
export interface Merkelapp {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  label?: any[];
  'sist-endret'?: string;
  'tilknyttede-fag'?: any[];
  'tilknyttede-laereplaner'?: any[];
  'tilknyttede-programomraader'?: any[];
  'kan-knyttes-til-fag'?: boolean;
  'kan-knyttes-til-laereplan'?: boolean;
  'kan-knyttes-til-programomraade'?: boolean;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Fag- og vitnemålsmerknader som kan benyttes ved dokumentasjon av opplæringen, angitt i retningslinjer for føring av vitnemål og kompetansebevis fra Utdanningsdirektoratet
 * @see http://psi.udir.no/ontologi/kl06/Merknad
 */
export interface Merknad {
  'grep-type'?: string;
  label?: any[];
  'url-data'?: string;
  id?: string;
  kode?: string;
  uri?: string;
  tittel?: any[];
  status?: string;
  'sist-endret'?: string;
  'relaterte-aarstrinn'?: any[];
  opplaeringsnivaa?: any[];
  kortform?: any[];
  'merknads-type'?: any;
  dokumenttype?: any[];
  'relaterte-fag'?: any[];
  gyldighetsperiode?: any;
  'krav-om-vedlegg'?: boolean;
  'merknad-bruksomraade'?: string;
}

/**
 * Element for å angi hvilken type merknad en merknad er,  enten fag- eller vitnemålsmerknad
 * @see http://psi.udir.no/ontologi/kl06/Merknadstype
 */
export interface Merknadstype {
  'grep-type'?: string;
  label?: any[];
  'url-data'?: string;
  id?: string;
  kode?: string;
  uri?: string;
  beskrivelse?: any[];
  kortform?: any[];
  status?: string;
  'sist-endret'?: string;
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Egenskap for fagkode for å angi om eksamen er sentralgitt, eller lokalt gitt (URIen til denne typen er også brukt som egenskap)
 * @see http://psi.udir.no/ontologi/kl06/oppgave
 */
export interface Oppgave {
  beskrivelse?: any[];
  uri?: string;
  'url-data'?: string;
  'grep-type'?: string;
  label?: any[];
  id?: string;
  kode?: string;
  kortform?: any[];
  status?: string;
  'sist-endret'?: string;
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Egenskap for fagkode for å angi hva en gruppe elever/lærlinger/praksiskandidater/deltakere på et gitt årstrinn skal undervises i
 * @see http://psi.udir.no/ontologi/kl06/opplaeringsfag
 */
export interface Opplaeringsfag {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  label?: any[];
  'sist-endret'?: string;
  merkelapper?: any[];
  'programomraader-referanse'?: any[];
  'laereplan-referanse'?: any[];
  'fagkode-referanser'?: any[];
  'fagomraade-referanser'?: any[];
  'fortsetter-opplaering-i-samme-kompetansemaalsett-som'?: any[];
  fagtype?: any;
  opplaeringsnivaa?: any;
  tilleggsopplysninger?: any[];
  'bygger-paa-fag'?: any[];
  'for-aarstrinn'?: any[];
  kortform?: any[];
  erstatter?: any[];
  'erstattes-av'?: any[];
}

/**
 * Egenskap for læreplan, fagtype og fag- og vitnemålsmerknader for å angi hvilke(t) opplæringsnivå den gjelder for
 * @see http://psi.udir.no/ontologi/kl06/opplaeringsnivaa
 */
export interface Opplaeringsnivaa {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  label?: any[];
  'sist-endret'?: string;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Egenskap for programområde for å angi hvor opplæringen skjer, enten i "Skole" eller "Bedrift"
 * @see http://psi.udir.no/ontologi/kl06/Opplaeringssted
 */
export interface Opplaeringssted {
  'grep-type'?: string;
  label?: any[];
  'url-data'?: string;
  id?: string;
  kode?: string;
  uri?: string;
  beskrivelse?: any[];
  kortform?: any[];
  status?: string;
  'sist-endret'?: string;
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Element som inneholder en pedagogisk tekst som ikke er en del av forskrifsteksten, men skrevet av læreplanforfatterne eller de som forvalter læreplanen for å forklare et ord eller uttrykk
 * @see http://psi.udir.no/ontologi/kl06/Ordforklaring_lk20
 */
export interface OrdforklaringLk20 {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  label?: any[];
  beskrivelse?: any[];
  'sist-endret'?: string;
  'tilhoerer-laereplan'?: any;
  rekkefoelge?: number;
}

/**
 * Delmengde av læreplan (LK06) for inndeling av det faglige innholdet i logiske blokker for læreplaner som har programfag i stedet for hovedområder
 * @see http://psi.udir.no/ontologi/kl06/programfag
 */
export interface Programfag {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  rekkefoelge?: number;
  beskrivelse?: any[];
  'underliggende-hovedomraader'?: any[];
  label?: any[];
}

/**
 * Fastsatt pakke av fag, med et gitt samlet årstimetall, og som tas under et utdanningsprogram
 * @see http://psi.udir.no/ontologi/kl06/Programomraade
 */
export interface Programomraade {
  'grep-type'?: string;
  label?: any[];
  'url-data'?: string;
  kode?: string;
  uri?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  status?: string;
  'sist-endret'?: string;
  merkelapper?: any[];
  'utdanningsprogram-referanse'?: any[];
  kortform?: any[];
  landslinje?: boolean;
  'landsdekkende-linje'?: boolean;
  'programomraade-type'?: any;
  aarstimer?: string;
  'aarstimer-samisk'?: string;
  'aarstimer-doeve-og-tunghoerte'?: string;
  'aarstimer-formgivningsfag'?: string;
  tilleggsopplysninger?: any[];
  'foerste-semester'?: any;
  'siste-semester'?: any;
  aarstrinn?: any;
  'bygger-paa-programomraade'?: any[];
  erstatter?: any[];
  'erstattes-av'?: any[];
  yrkestittel?: any[];
  opplaeringssted?: any[];
  sluttkompetanse?: any[];
  opplaeringstid?: string;
  verdiskapingstid?: string;
  loepstype?: string;
}

/**
 * Instans av programområdetype, enten Bedrift(Lærling), Skole(Elev) eller Særløp
 * @see http://psi.udir.no/ontologi/kl06/Programomraadetype
 */
export interface Programomraadetype {
  'grep-type'?: string;
  label?: any[];
  'url-data'?: string;
  id?: string;
  kode?: string;
  uri?: string;
  beskrivelse?: any[];
  kortform?: any[];
  status?: string;
  'sist-endret'?: string;
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Tidsperiode som viser til et konkret skolesemester i et gitt skoleår, f.eks. vår 2016
 * @see http://psi.udir.no/ontologi/kl06/Semester
 */
export interface Semester {
  beskrivelse?: any[];
  uri?: string;
  'url-data'?: string;
  'grep-type'?: string;
  label?: any[];
  id?: string;
  kode?: string;
  tittel?: any[];
  status?: string;
  'sist-endret'?: string;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Property for "fagkode" (subject code) to specify whether the censorship is managed centrally or locally
 * @see http://psi.udir.no/ontologi/kl06/sensur
 */
export interface Sensur {
  beskrivelse?: any[];
  uri?: string;
  'url-data'?: string;
  'grep-type'?: string;
  label?: any[];
  id?: string;
  kode?: string;
  kortform?: any[];
  status?: string;
  'sist-endret'?: string;
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Egenskap for programområde for å angi om eleven/lærlingen eller praksiskandidaten oppnår studiekompetanse, yrkeskompetanse eller et fag- eller svennebrev etter endt utdanning
 * @see http://psi.udir.no/ontologi/kl06/sluttkompetanse
 */
export interface Sluttkompetanse {
  'grep-type'?: string;
  label?: any[];
  'url-data'?: string;
  beskrivelse?: any[];
  uri?: string;
  id?: string;
  kode?: string;
  kortform?: any[];
  status?: string;
  'sist-endret'?: string;
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Klasse for å holde på språk for løsningen
 * @see http://psi.udir.no/ontologi/kl06/Spraak
 */
export interface Spraak {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  label?: any[];
  'sist-endret'?: string;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Egenskap for fagkoder som er språkfag, for å angi nivåer etter CEFR-rammeverket
 * @see http://psi.udir.no/ontologi/kl06/spraaknivaa
 */
export interface Spraaknivaa {
  id?: string;
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: any[];
  'grep-type'?: string;
  status?: string;
  'sist-endret'?: string;
  cefr?: string;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
  label?: any[];
}

/**
 * Egenskap som angir om elementet det opptrer i er “Publisert” (del av gjeldende tilbud), eller “Utgått” (ikke lenger tilbudt)
 * @see http://psi.udir.no/ontologi/kl06/status
 */
export interface Status {
  'grep-type'?: string;
  label?: any[];
  'url-data'?: string;
  id?: string;
  kode?: string;
  uri?: string;
  tittel?: any[];
  status?: string;
  'sist-endret'?: string;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Element som bærer informasjon om tidligere tittrl/navn/ordlyd på enten Utdanningsprogram, Programomraade eller Merknad, perioden disse egenskapene gjaldt, samt referanse til objektene som gjelder i dag.
 * @see http://psi.udir.no/ontologi/kl06/Tidligere_navn
 */
export interface TidligereNavn {
  'grep-type'?: string;
  label?: any[];
  'url-data'?: string;
  id?: string;
  kode?: string;
  uri?: string;
  tittel?: any[];
  status?: string;
  'sist-endret'?: string;
  'tidligere-navn-for'?: any;
}

/**
 * Element for å angi om faget er trekkfag eller om det er obligatorisk eksamen
 * @see http://psi.udir.no/ontologi/kl06/Trekkordning
 */
export interface Trekkordning {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  label?: any[];
  'sist-endret'?: string;
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Element som beskriver hver av de tre prioriterte temaene folkehelse og lvsmestring, demokrati og medborgerskap og bærekraftig utvikling (forekommer i de enkelte læreplanene der de er ansett som aktuelle for for faget, og har der sin egen fagspesifikke beskrivelse)
 * @see http://psi.udir.no/ontologi/kl06/Tverrfaglig_tema_lk20
 */
export interface TverrfagligTemaLk20 {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  label?: any[];
  'lenke-til-beskrivelse'?: string;
  rekkefoelge?: number;
  'sist-endret'?: string;
}

/**
 * Utdanningsløp i videregående utdanning som fører fram til studie- og eller yrkeskompetanse/fag- eller svennebrev jf. Rundskriv Udir-1-[et gitt årstall]
 * @see http://psi.udir.no/ontologi/kl06/Utdanningsprogram
 */
export interface Utdanningsprogram {
  'grep-type'?: string;
  label?: any[];
  'url-data'?: string;
  kode?: string;
  uri?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  status?: string;
  'tidligere-navn'?: any[];
  'sist-endret'?: string;
  kortform?: any[];
  'type-utdanningsprogram'?: any;
  tilleggsopplysninger?: any[];
  erstatter?: any[];
  'erstattes-av'?: any[];
  'foerste-semester'?: any;
  'siste-semester'?: string;
}

/**
 * Element for utdanningsprogram for å angi om utdanningsprogrammet enten er Studieforberedende utdanningsprogram eller Yrkesfaglig utdanningsprogram
 * @see http://psi.udir.no/ontologi/kl06/Utdanningsprogramtype
 */
export interface Utdanningsprogramtype {
  'grep-type'?: string;
  label?: any[];
  'url-data'?: string;
  id?: string;
  kode?: string;
  uri?: string;
  beskrivelse?: any[];
  kortform?: any[];
  status?: string;
  'sist-endret'?: string;
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

/**
 * Bestanddel av læreplan som uttrykker anvendelse av kunnskaper og ferdigheter, og som i læreplanvisningen på udir.no er implementert slik at disse opptrer som ordforklaring til forekomster av utvalgte verb i læreplanens kompetansemål
 * @see http://psi.udir.no/ontologi/kl06/Verb_lk20
 */
export interface VerbLk20 {
  'grep-type'?: string;
  label?: any[];
  'url-data'?: string;
  beskrivelse?: any[];
  'globalt-verb'?: boolean;
  id?: string;
  kode?: string;
  uri?: string;
  tittel?: any[];
  status?: string;
  'sist-endret'?: string;
  'tilhoerer-laereplan'?: any;
  rekkefoelge?: number;
}

/**
 * Element for vurderingsordning for å angi om det skal gis tallkarakterer eller om det skal benyttes andre uttrykk for vurderingen
 * @see http://psi.udir.no/ontologi/kl06/Vurderingsuttrykk
 */
export interface Vurderingsuttrykk {
  kode?: string;
  uri?: string;
  'url-data'?: string;
  tittel?: string;
  gyldighet?: any;
  id?: string;
  'grep-type'?: string;
  status?: string;
  label?: any[];
  'sist-endret'?: string;
  'tillatte-uttrykk'?: any[];
  kortform?: any[];
  'gyldig-fra'?: string;
  'gyldig-til'?: string;
  rekkefoelge?: number;
}

