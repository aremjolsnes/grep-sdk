# AUTOGENERERT FIL
from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict

class Aarstrinn(BaseModel):
    """
    Utdanningsnivå som angir progresjon for det 13-årige utdanningsløpet
    Se: http://psi.udir.no/ontologi/kl06/aarstrinn
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    numerisk_verdi: Optional[float] = Field(None, alias="numerisk-verdi")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None
    gyldighet: Optional[Dict[str, Any]] = None
    label: Optional[List[Any]] = None

class Dokumenttype(BaseModel):
    """
    Egenskap for merknad for å angi om den gjelder for enten “Vitnemål” eller “Kompetansebevis”
    Se: http://psi.udir.no/ontologi/kl06/dokumenttype
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    beskrivelse: Optional[List[Any]] = None
    kortform: Optional[List[Any]] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None
    label: Optional[List[Any]] = None

class Eksamensform(BaseModel):
    """
    Element for å angi hvilken eksamensform som skal påføres vitnemålet
    Se: http://psi.udir.no/ontologi/kl06/eksamensform
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None
    gyldighet: Optional[Dict[str, Any]] = None
    label: Optional[List[Any]] = None

class Eksamensordning(BaseModel):
    """
    Element for å angi hva slags eksamensordning som gjelder for elever og privatister
    Se: http://psi.udir.no/ontologi/kl06/eksamensordning
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None
    gyldighet: Optional[Dict[str, Any]] = None
    label: Optional[List[Any]] = None

class Fagkategori(BaseModel):
    """
    Egenskap for fagområde for å angi hierarkisk overordnet faglig innholdskategori (for statistisk bruk)
    Se: http://psi.udir.no/ontologi/kl06/fagkategori
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    gyldighet: Optional[Dict[str, Any]] = None
    label: Optional[List[Any]] = None

class Fagkode(BaseModel):
    """
    Element som fungerer som identifikator for et fag eller del av et fag, for presist å kunne angi opplæring, eksamensgjennomføring, vurdering og dokumentasjon, for eksempel MAT0011 "Matematikk 10.årstrinn, muntlig"
    Se: http://psi.udir.no/ontologi/kl06/fagkode
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    merkelapper: Optional[List[Any]] = None
    vurderingsordning: Optional[List[Any]] = None
    opplaeringsfag: Optional[List[Any]] = None
    tilleggseksamen_ikke_normalt_loep: Optional[List[Any]] = Field(None, alias="tilleggseksamen-ikke-normalt-loep")
    benyttes_sammen_med: Optional[List[Any]] = Field(None, alias="benyttes-sammen-med")
    spraaknivaa: Optional[str] = None
    erstatter: Optional[List[Any]] = None
    erstattes_av: Optional[List[Any]] = Field(None, alias="erstattes-av")
    omfang_totalt: Optional[str] = Field(None, alias="omfang-totalt")
    omfang_vitnemaal: Optional[str] = Field(None, alias="omfang-vitnemaal")
    omfang_til_naa: Optional[str] = Field(None, alias="omfang-til-naa")
    naar_kan_man_ta_eksamen: Optional[Dict[str, Any]] = Field(None, alias="naar-kan-man-ta-eksamen")
    naar_gis_det_undervisning: Optional[Dict[str, Any]] = Field(None, alias="naar-gis-det-undervisning")
    sensur: Optional[Dict[str, Any]] = None
    oppgave: Optional[Dict[str, Any]] = None
    tilleggsopplysninger: Optional[List[Any]] = None
    bygger_paa_fag: Optional[List[Any]] = Field(None, alias="bygger-paa-fag")
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    iso_639_2_kode: Optional[str] = Field(None, alias="iso-639-2-kode")
    fagtype: Optional[Dict[str, Any]] = None
    opplaeringsnivaa: Optional[Dict[str, Any]] = None
    kortform: Optional[List[Any]] = None
    gyldighet: Optional[Dict[str, Any]] = None
    label: Optional[List[Any]] = None

class Fagomraade(BaseModel):
    """
    Gruppering av opplæringsfag i faglige innholdskategorier under fagketegorier (se fagkategori) for statistisk bruk
    Se: http://psi.udir.no/ontologi/kl06/fagomraade
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    fagkategori: Optional[List[Any]] = None
    label: Optional[List[Any]] = None
    gyldighet: Optional[Dict[str, Any]] = None

class Fagtype(BaseModel):
    """
    Gruppering av fag etter Rundskriv Udir-1-[et gitt årstall]
    Se: http://psi.udir.no/ontologi/kl06/fagtype
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    opplaeringsnivaa: Optional[Dict[str, Any]] = None
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None
    label: Optional[List[Any]] = None

class GrunnleggendeFerdighetLk20(BaseModel):
    """
    Den delmengden av den totale kompetansen i fag som handler å vise de fem utvalgte ferdighetene: Å kunne lese, å kunne skrive, å kunne regne, muntlige og digitale ferdiheter
    Se: http://psi.udir.no/ontologi/kl06/grunnleggende_ferdighet_lk20
    """
    lenke_til_beskrivelse: Optional[str] = Field(None, alias="lenke-til-beskrivelse")
    rekkefoelge: Optional[float] = None
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    gyldighet: Optional[Dict[str, Any]] = None
    label: Optional[List[Any]] = None

class Hovedomraade(BaseModel):
    """
    Delmengde av læreplan for inndeling av det faglige innholdet i logiske blokker
    Se: http://psi.udir.no/ontologi/kl06/hovedomraade
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    beskrivelse: Optional[List[Any]] = None
    underliggende_hovedomraader: Optional[List[Any]] = Field(None, alias="underliggende-hovedomraader")
    rekkefoelge: Optional[float] = None
    gyldighet: Optional[Dict[str, Any]] = None
    status: Optional[str] = None
    label: Optional[List[Any]] = None

class Karakter(BaseModel):
    """
    Grep-type som brukes av andre systemer som autoritetsregister til å angi lovlige karakteruttrykk i dokumentasjon (vitnemål o.l), f.eks. "BESTÅTT", "FEM", "IKKE BESTÅTT"
    Se: http://psi.udir.no/ontologi/kl06/karakter
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None
    label: Optional[List[Any]] = None
    gyldighet: Optional[Dict[str, Any]] = None

class KjerneelementLk20(BaseModel):
    """
    Element som sammen med de andre i samme læreplan, uttrykker hva som er det viktigste i faget og hva elevene/lærlingene/praksiskandidatene må lære for å mestre og bruke faget (kan være kunnskapsområder, metoder, begreper, tenkemåter og uttrykksformer)
    Se: http://psi.udir.no/ontologi/kl06/kjerneelement_lk20
    """
    rekkefoelge: Optional[float] = None
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    beskrivelse: Optional[Dict[str, Any]] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    forklaring: Optional[List[Any]] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    tilhoerer_laereplan: Optional[Dict[str, Any]] = Field(None, alias="tilhoerer-laereplan")
    gyldighet: Optional[Dict[str, Any]] = None
    label: Optional[List[Any]] = None

class Kompetansemaal(BaseModel):
    """
    Element (for læreplaner i LK06) som angir en delmengde av den kompetanse en elev/lærling/praksiskandidat skal ha oppnådd etter endt opplæring på et gitt nivå/trinn
    Se: kompetansemaal
    """
    rekkefoelge: Optional[float] = None
    tilhoerer_hovedomraade: Optional[Dict[str, Any]] = Field(None, alias="tilhoerer-hovedomraade")
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    laereplan_referanser: Optional[List[Any]] = Field(None, alias="laereplan-referanser")
    label: Optional[List[Any]] = None

class KompetansemaalLk20(BaseModel):
    """
    Element (for læreplaner i LK20) som angir en delmengde av den kompetanse en elev/lærling/praksiskandidat/deltaker skal ha oppnådd etter endt opplæring på et gitt nivå/trinn
    Se: http://psi.udir.no/ontologi/kl06/kompetansemaal_lk20
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    rekkefoelge: Optional[float] = None
    tilknyttede_tverrfaglige_temaer: Optional[List[Any]] = Field(None, alias="tilknyttede-tverrfaglige-temaer")
    tilknyttede_kjerneelementer: Optional[List[Any]] = Field(None, alias="tilknyttede-kjerneelementer")
    tilknyttede_grunnleggende_ferdigheter: Optional[List[Any]] = Field(None, alias="tilknyttede-grunnleggende-ferdigheter")
    tilknyttede_verb: Optional[List[Any]] = Field(None, alias="tilknyttede-verb")
    bygger_paa: Optional[List[Any]] = Field(None, alias="bygger-paa")
    samme_som: Optional[List[Any]] = Field(None, alias="samme-som")
    tilhoerer_kompetansemaalsett: Optional[Dict[str, Any]] = Field(None, alias="tilhoerer-kompetansemaalsett")
    tilhoerer_laereplan: Optional[Dict[str, Any]] = Field(None, alias="tilhoerer-laereplan")
    gjenbruk_av: Optional[str] = Field(None, alias="gjenbruk-av")
    hentet_fra: Optional[Dict[str, Any]] = Field(None, alias="hentet-fra")
    forklaring: Optional[List[Any]] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    label: Optional[List[Any]] = None

class Kompetansemaalsett(BaseModel):
    """
    Egenskap for 'Laereplan' og 'Laereplan_lk20' for å angi hvilke competence aim set den består av
    Se: http://psi.udir.no/ontologi/kl06/kompetansemaalsett
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    etter_fag: Optional[List[Any]] = Field(None, alias="etter-fag")
    programfag: Optional[Dict[str, Any]] = None
    hovedomraader_i_kontekst_av_kompetansemaalsett: Optional[List[Any]] = Field(None, alias="hovedomraader-i-kontekst-av-kompetansemaalsett")
    kompetansemaal: Optional[List[Any]] = None
    tilhoerer_laereplan: Optional[Dict[str, Any]] = Field(None, alias="tilhoerer-laereplan")
    maal_for_kompetansemaalene_overskrift: Optional[List[Any]] = Field(None, alias="maal-for-kompetansemaalene-overskrift")
    benyttes_paa_aarstrinn: Optional[List[Any]] = Field(None, alias="benyttes-paa-aarstrinn")
    etter_aarstrinn: Optional[List[Any]] = Field(None, alias="etter-aarstrinn")
    gyldighet: Optional[Dict[str, Any]] = None
    status: Optional[str] = None
    rekkefoelge: Optional[float] = None
    label: Optional[List[Any]] = None

class KompetansemaalsettLk20(BaseModel):
    """
    Et sett med kompetansemål som gjelder for et spesifisert sett med trinn eller nivåer
    Se: http://psi.udir.no/ontologi/kl06/kompetansemaalsett_lk20
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    kortform: Optional[List[Any]] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    rekkefoelge: Optional[float] = None
    forklaring: Optional[List[Any]] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    kompetansemaal_overskrift: Optional[Dict[str, Any]] = Field(None, alias="kompetansemaal-overskrift")
    kompetansemaal_ingress: Optional[Dict[str, Any]] = Field(None, alias="kompetansemaal-ingress")
    kompetansemaal: Optional[List[Any]] = None
    underveisvurdering: Optional[Dict[str, Any]] = None
    standpunktvurdering: Optional[Dict[str, Any]] = None
    etter_fag: Optional[List[Any]] = Field(None, alias="etter-fag")
    etter_aarstrinn: Optional[List[Any]] = Field(None, alias="etter-aarstrinn")
    benyttes_paa_aarstrinn: Optional[List[Any]] = Field(None, alias="benyttes-paa-aarstrinn")
    tilhoerer_laereplan: Optional[Dict[str, Any]] = Field(None, alias="tilhoerer-laereplan")
    gyldighet: Optional[Dict[str, Any]] = None
    label: Optional[List[Any]] = None

class Laereplan(BaseModel):
    """
    Element som uttrykker den samlede kompetansen en elev, lærling eller lærekandidat skal ha etter endt opplæring på et gitt nivå/trinn i ett eller flere fag etter Kunnskapsløftet LK06)
    Se: http://psi.udir.no/ontologi/kl06/laereplan
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    tilhoerende_kompetansemaalsett: Optional[List[Any]] = Field(None, alias="tilhoerende-kompetansemaalsett")
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    merkelapper: Optional[List[Any]] = None
    programfag_kapittel: Optional[Dict[str, Any]] = Field(None, alias="programfag-kapittel")
    hovedomraade_kapittel: Optional[str] = Field(None, alias="hovedomraade-kapittel")
    kompetansemaal_kapittel: Optional[Dict[str, Any]] = Field(None, alias="kompetansemaal-kapittel")
    fastsettelsesinformasjon: Optional[Dict[str, Any]] = None
    fagtype: Optional[List[Any]] = None
    tilgjengelige_spraak: Optional[List[Any]] = Field(None, alias="tilgjengelige-spraak")
    opplaeringsnivaa: Optional[List[Any]] = None
    gyldighetsperiode: Optional[Dict[str, Any]] = None
    erstatter: Optional[List[Any]] = None
    erstattes_av: Optional[List[Any]] = Field(None, alias="erstattes-av")
    formaal_kapittel: Optional[Dict[str, Any]] = Field(None, alias="formaal-kapittel")
    timetall_kapittel: Optional[Dict[str, Any]] = Field(None, alias="timetall-kapittel")
    struktur_kapittel: Optional[Dict[str, Any]] = Field(None, alias="struktur-kapittel")
    grunnleggende_ferdigheter_kapittel: Optional[Dict[str, Any]] = Field(None, alias="grunnleggende-ferdigheter-kapittel")
    vurdering_kapittel: Optional[Dict[str, Any]] = Field(None, alias="vurdering-kapittel")
    siste_eksamen: Optional[str] = Field(None, alias="siste-eksamen")
    soekehjelp_navn_motsatt_maalform: Optional[str] = Field(None, alias="soekehjelp-navn-motsatt-maalform")
    tilleggsopplysninger: Optional[str] = None
    label: Optional[List[Any]] = None

class LaereplanLk20(BaseModel):
    """
    Element som uttrykker den samlede kompetansen en elev, lærling,  lærekandidat eller deltaker skal ha etter endt opplæring på et gitt nivå/trinn i ett eller flere fag etter Kunnskapsløftet LK20, fagfornyelsen
    Se: http://psi.udir.no/ontologi/kl06/laereplan_lk20
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    kortform: Optional[List[Any]] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    laereplanstruktur: Optional[Dict[str, Any]] = None
    fastsettelsesinformasjon: Optional[Dict[str, Any]] = None
    fagtype: Optional[List[Any]] = None
    tilgjengelige_spraak: Optional[List[Any]] = Field(None, alias="tilgjengelige-spraak")
    opplaeringsnivaa: Optional[List[Any]] = None
    ordforklaringer: Optional[List[Any]] = None
    gyldighetsperiode: Optional[Dict[str, Any]] = None
    erstatter: Optional[List[Any]] = None
    erstattes_av: Optional[List[Any]] = Field(None, alias="erstattes-av")
    siste_eksamen: Optional[str] = Field(None, alias="siste-eksamen")
    merkelapper: Optional[List[Any]] = None
    om_faget_kapittel: Optional[Dict[str, Any]] = Field(None, alias="om-faget-kapittel")
    kompetansemaal_kapittel: Optional[Dict[str, Any]] = Field(None, alias="kompetansemaal-kapittel")
    vurderingsordning_kapittel: Optional[Dict[str, Any]] = Field(None, alias="vurderingsordning-kapittel")
    vurderingsordninger_kapittel: Optional[Dict[str, Any]] = Field(None, alias="vurderingsordninger-kapittel")
    tilleggsopplysninger: Optional[List[Any]] = None
    opprinnelige_planer: Optional[List[Any]] = Field(None, alias="opprinnelige-planer")
    label: Optional[List[Any]] = None
    tilhoerende_kompetansemaalsett: Optional[List[Any]] = Field(None, alias="tilhoerende-kompetansemaalsett")

class Laereplanstruktur(BaseModel):
    """
    Egenskap for læreplan (lk20) for å angi om hvilken struktur den følger (foreløpig) enten "vanlig" (strukturert etter årstrinn/fag) eller "modulstrukturert" (strukturert etter angitte moduler)
    Se: http://psi.udir.no/ontologi/kl06/laereplanstruktur
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None
    gyldighet: Optional[Dict[str, Any]] = None
    label: Optional[List[Any]] = None

class Loepstype(BaseModel):
    """
    Element for "programomraade" for å angi hvilken løpstype det er (p.t. er kun kryssløp tilgjengelig). Se også egenskapen "loepstype-kryssloep"
    Se: http://psi.udir.no/ontologi/kl06/loepstype
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    beskrivelse: Optional[List[Any]] = None
    kortform: Optional[List[Any]] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None
    label: Optional[List[Any]] = None

class Merkelapp(BaseModel):
    """
    Element for å angi spesifikke egenskaper for forekomster av fagkode, laereplan,  laereplan_lk20, opplaeringsfag og programomraade
    Se: http://psi.udir.no/ontologi/kl06/merkelapp
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    label: Optional[List[Any]] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    tilknyttede_fag: Optional[List[Any]] = Field(None, alias="tilknyttede-fag")
    tilknyttede_laereplaner: Optional[List[Any]] = Field(None, alias="tilknyttede-laereplaner")
    tilknyttede_programomraader: Optional[List[Any]] = Field(None, alias="tilknyttede-programomraader")
    kan_knyttes_til_fag: Optional[bool] = Field(None, alias="kan-knyttes-til-fag")
    kan_knyttes_til_laereplan: Optional[bool] = Field(None, alias="kan-knyttes-til-laereplan")
    kan_knyttes_til_programomraade: Optional[bool] = Field(None, alias="kan-knyttes-til-programomraade")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class Merknad(BaseModel):
    """
    Fag- og vitnemålsmerknader som kan benyttes ved dokumentasjon av opplæringen, angitt i retningslinjer for føring av vitnemål og kompetansebevis fra Utdanningsdirektoratet
    Se: http://psi.udir.no/ontologi/kl06/merknad
    """
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    tittel: Optional[Any] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    relaterte_aarstrinn: Optional[List[Any]] = Field(None, alias="relaterte-aarstrinn")
    opplaeringsnivaa: Optional[List[Any]] = None
    kortform: Optional[List[Any]] = None
    merknads_type: Optional[Dict[str, Any]] = Field(None, alias="merknads-type")
    dokumenttype: Optional[List[Any]] = None
    relaterte_fag: Optional[List[Any]] = Field(None, alias="relaterte-fag")
    gyldighetsperiode: Optional[Dict[str, Any]] = None
    krav_om_vedlegg: Optional[bool] = Field(None, alias="krav-om-vedlegg")
    merknad_bruksomraade: Optional[str] = Field(None, alias="merknad-bruksomraade")

class Merknadstype(BaseModel):
    """
    Element for å angi hvilken type merknad en merknad er,  enten fag- eller vitnemålsmerknad
    Se: http://psi.udir.no/ontologi/kl06/merknadstype
    """
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    beskrivelse: Optional[List[Any]] = None
    kortform: Optional[List[Any]] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class Oppgave(BaseModel):
    """
    Egenskap for fagkode for å angi om eksamen er sentralgitt, eller lokalt gitt (URIen til denne typen er også brukt som egenskap)
    Se: http://psi.udir.no/ontologi/kl06/oppgave
    """
    beskrivelse: Optional[List[Any]] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    id: Optional[str] = None
    kode: Optional[str] = None
    kortform: Optional[List[Any]] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class Opplaeringsfag(BaseModel):
    """
    Egenskap for fagkode for å angi hva en gruppe elever/lærlinger/praksiskandidater/deltakere på et gitt årstrinn skal undervises i
    Se: http://psi.udir.no/ontologi/kl06/opplaeringsfag
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    label: Optional[List[Any]] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    merkelapper: Optional[List[Any]] = None
    programomraader_referanse: Optional[List[Any]] = Field(None, alias="programomraader-referanse")
    laereplan_referanse: Optional[List[Any]] = Field(None, alias="laereplan-referanse")
    fagkode_referanser: Optional[List[Any]] = Field(None, alias="fagkode-referanser")
    fagomraade_referanser: Optional[List[Any]] = Field(None, alias="fagomraade-referanser")
    fortsetter_opplaering_i_samme_kompetansemaalsett_som: Optional[List[Any]] = Field(None, alias="fortsetter-opplaering-i-samme-kompetansemaalsett-som")
    fagtype: Optional[Dict[str, Any]] = None
    opplaeringsnivaa: Optional[Dict[str, Any]] = None
    tilleggsopplysninger: Optional[List[Any]] = None
    bygger_paa_fag: Optional[List[Any]] = Field(None, alias="bygger-paa-fag")
    for_aarstrinn: Optional[List[Any]] = Field(None, alias="for-aarstrinn")
    kortform: Optional[List[Any]] = None
    erstatter: Optional[List[Any]] = None
    erstattes_av: Optional[List[Any]] = Field(None, alias="erstattes-av")

class Opplaeringsnivaa(BaseModel):
    """
    Egenskap for læreplan, fagtype og fag- og vitnemålsmerknader for å angi hvilke(t) opplæringsnivå den gjelder for
    Se: http://psi.udir.no/ontologi/kl06/opplaeringsnivaa
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    label: Optional[List[Any]] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class Opplaeringssted(BaseModel):
    """
    Egenskap for programområde for å angi hvor opplæringen skjer, enten i "Skole" eller "Bedrift"
    Se: http://psi.udir.no/ontologi/kl06/opplaeringssted
    """
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    beskrivelse: Optional[List[Any]] = None
    kortform: Optional[List[Any]] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class OrdforklaringLk20(BaseModel):
    """
    Element som inneholder en pedagogisk tekst som ikke er en del av forskrifsteksten, men skrevet av læreplanforfatterne eller de som forvalter læreplanen for å forklare et ord eller uttrykk
    Se: http://psi.udir.no/ontologi/kl06/ordforklaring_lk20
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    label: Optional[List[Any]] = None
    beskrivelse: Optional[List[Any]] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    tilhoerer_laereplan: Optional[Dict[str, Any]] = Field(None, alias="tilhoerer-laereplan")
    rekkefoelge: Optional[float] = None

class Programfag(BaseModel):
    """
    Delmengde av læreplan (LK06) for inndeling av det faglige innholdet i logiske blokker for læreplaner som har programfag i stedet for hovedområder
    Se: http://psi.udir.no/ontologi/kl06/programfag
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    rekkefoelge: Optional[float] = None
    beskrivelse: Optional[List[Any]] = None
    underliggende_hovedomraader: Optional[List[Any]] = Field(None, alias="underliggende-hovedomraader")
    label: Optional[List[Any]] = None

class Programomraade(BaseModel):
    """
    Fastsatt pakke av fag, med et gitt samlet årstimetall, og som tas under et utdanningsprogram
    Se: http://psi.udir.no/ontologi/kl06/programomraade
    """
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    kode: Optional[str] = None
    uri: Optional[str] = None
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    merkelapper: Optional[List[Any]] = None
    utdanningsprogram_referanse: Optional[List[Any]] = Field(None, alias="utdanningsprogram-referanse")
    kortform: Optional[List[Any]] = None
    landslinje: Optional[bool] = None
    landsdekkende_linje: Optional[bool] = Field(None, alias="landsdekkende-linje")
    programomraade_type: Optional[Dict[str, Any]] = Field(None, alias="programomraade-type")
    aarstimer: Optional[str] = None
    aarstimer_samisk: Optional[str] = Field(None, alias="aarstimer-samisk")
    aarstimer_doeve_og_tunghoerte: Optional[str] = Field(None, alias="aarstimer-doeve-og-tunghoerte")
    aarstimer_formgivningsfag: Optional[str] = Field(None, alias="aarstimer-formgivningsfag")
    tilleggsopplysninger: Optional[List[Any]] = None
    foerste_semester: Optional[Dict[str, Any]] = Field(None, alias="foerste-semester")
    siste_semester: Optional[Dict[str, Any]] = Field(None, alias="siste-semester")
    aarstrinn: Optional[Dict[str, Any]] = None
    bygger_paa_programomraade: Optional[List[Any]] = Field(None, alias="bygger-paa-programomraade")
    erstatter: Optional[List[Any]] = None
    erstattes_av: Optional[List[Any]] = Field(None, alias="erstattes-av")
    yrkestittel: Optional[List[Any]] = None
    opplaeringssted: Optional[List[Any]] = None
    sluttkompetanse: Optional[List[Any]] = None
    opplaeringstid: Optional[str] = None
    verdiskapingstid: Optional[str] = None
    loepstype: Optional[str] = None

class Programomraadetype(BaseModel):
    """
    Instans av programområdetype, enten Bedrift(Lærling), Skole(Elev) eller Særløp
    Se: http://psi.udir.no/ontologi/kl06/programomraadetype
    """
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    beskrivelse: Optional[List[Any]] = None
    kortform: Optional[List[Any]] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class Semester(BaseModel):
    """
    Tidsperiode som viser til et konkret skolesemester i et gitt skoleår, f.eks. vår 2016
    Se: http://psi.udir.no/ontologi/kl06/semester
    """
    beskrivelse: Optional[List[Any]] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    id: Optional[str] = None
    kode: Optional[str] = None
    tittel: Optional[Any] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class Sensur(BaseModel):
    """
    Egenskap for fagkode for å angi om sensuren er administrert sentralt eller lokalt
    Se: http://psi.udir.no/ontologi/kl06/sensur
    """
    beskrivelse: Optional[List[Any]] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    id: Optional[str] = None
    kode: Optional[str] = None
    kortform: Optional[List[Any]] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class Sluttkompetanse(BaseModel):
    """
    Egenskap for programområde for å angi om eleven/lærlingen eller praksiskandidaten oppnår studiekompetanse, yrkeskompetanse eller et fag- eller svennebrev etter endt utdanning
    Se: http://psi.udir.no/ontologi/kl06/sluttkompetanse
    """
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    beskrivelse: Optional[List[Any]] = None
    uri: Optional[str] = None
    id: Optional[str] = None
    kode: Optional[str] = None
    kortform: Optional[List[Any]] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class Spraak(BaseModel):
    """
    Klasse for å holde på språk for løsningen
    Se: http://psi.udir.no/ontologi/kl06/spraak
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    label: Optional[List[Any]] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class Spraaknivaa(BaseModel):
    """
    Egenskap for fagkoder som er språkfag, for å angi nivåer etter CEFR-rammeverket
    Se: http://psi.udir.no/ontologi/kl06/spraaknivaa
    """
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    cefr: Optional[str] = None
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None
    label: Optional[List[Any]] = None

class Status(BaseModel):
    """
    Egenskap som angir om elementet det opptrer i er “Publisert” (del av gjeldende tilbud), eller “Utgått” (ikke lenger tilbudt)
    Se: http://psi.udir.no/ontologi/kl06/status
    """
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    tittel: Optional[Any] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class TidligereNavn(BaseModel):
    """
    Element som bærer informasjon om tidligere tittrl/navn/ordlyd på enten Utdanningsprogram, Programomraade eller Merknad, perioden disse egenskapene gjaldt, samt referanse til objektene som gjelder i dag.
    Se: http://psi.udir.no/ontologi/kl06/tidligere_navn
    """
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    tittel: Optional[Any] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    tidligere_navn_for: Optional[Dict[str, Any]] = Field(None, alias="tidligere-navn-for")

class Trekkordning(BaseModel):
    """
    Element for å angi om faget er trekkfag eller om det er obligatorisk eksamen
    Se: http://psi.udir.no/ontologi/kl06/trekkordning
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    label: Optional[List[Any]] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class TverrfagligTemaLk20(BaseModel):
    """
    Element som beskriver hver av de tre prioriterte temaene folkehelse og lvsmestring, demokrati og medborgerskap og bærekraftig utvikling (forekommer i de enkelte læreplanene der de er ansett som aktuelle for for faget, og har der sin egen fagspesifikke beskrivelse)
    Se: http://psi.udir.no/ontologi/kl06/tverrfaglig_tema_lk20
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    label: Optional[List[Any]] = None
    lenke_til_beskrivelse: Optional[str] = Field(None, alias="lenke-til-beskrivelse")
    rekkefoelge: Optional[float] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")

class Utdanningsprogram(BaseModel):
    """
    Utdanningsløp i videregående utdanning som fører fram til studie- og eller yrkeskompetanse/fag- eller svennebrev jf. Rundskriv Udir-1-[et gitt årstall]
    Se: http://psi.udir.no/ontologi/kl06/utdanningsprogram
    """
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    kode: Optional[str] = None
    uri: Optional[str] = None
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    status: Optional[str] = None
    tidligere_navn: Optional[List[Any]] = Field(None, alias="tidligere-navn")
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    kortform: Optional[List[Any]] = None
    type_utdanningsprogram: Optional[Dict[str, Any]] = Field(None, alias="type-utdanningsprogram")
    tilleggsopplysninger: Optional[List[Any]] = None
    erstatter: Optional[List[Any]] = None
    erstattes_av: Optional[List[Any]] = Field(None, alias="erstattes-av")
    foerste_semester: Optional[Dict[str, Any]] = Field(None, alias="foerste-semester")
    siste_semester: Optional[str] = Field(None, alias="siste-semester")

class Utdanningsprogramtype(BaseModel):
    """
    Element for utdanningsprogram for å angi om utdanningsprogrammet enten er Studieforberedende utdanningsprogram eller Yrkesfaglig utdanningsprogram
    Se: http://psi.udir.no/ontologi/kl06/utdanningsprogramtype
    """
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    beskrivelse: Optional[List[Any]] = None
    kortform: Optional[List[Any]] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

class VerbLk20(BaseModel):
    """
    Bestanddel av læreplan som uttrykker anvendelse av kunnskaper og ferdigheter, og som i læreplanvisningen på udir.no er implementert slik at disse opptrer som ordforklaring til forekomster av utvalgte verb i læreplanens kompetansemål
    Se: http://psi.udir.no/ontologi/kl06/verb_lk20
    """
    grep_type: Optional[str] = Field(None, alias="grep-type")
    label: Optional[List[Any]] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    beskrivelse: Optional[List[Any]] = None
    globalt_verb: Optional[bool] = Field(None, alias="globalt-verb")
    id: Optional[str] = None
    kode: Optional[str] = None
    uri: Optional[str] = None
    tittel: Optional[Any] = None
    status: Optional[str] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    tilhoerer_laereplan: Optional[Dict[str, Any]] = Field(None, alias="tilhoerer-laereplan")
    rekkefoelge: Optional[float] = None

class Vurderingsuttrykk(BaseModel):
    """
    Element for vurderingsordning for å angi om det skal gis tallkarakterer eller om det skal benyttes andre uttrykk for vurderingen
    Se: http://psi.udir.no/ontologi/kl06/vurderingsuttrykk
    """
    kode: Optional[str] = None
    uri: Optional[str] = None
    url_data: Optional[str] = Field(None, alias="url-data")
    tittel: Optional[Any] = None
    gyldighet: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    grep_type: Optional[str] = Field(None, alias="grep-type")
    status: Optional[str] = None
    label: Optional[List[Any]] = None
    sist_endret: Optional[str] = Field(None, alias="sist-endret")
    tillatte_uttrykk: Optional[List[Any]] = Field(None, alias="tillatte-uttrykk")
    kortform: Optional[List[Any]] = None
    gyldig_fra: Optional[str] = Field(None, alias="gyldig-fra")
    gyldig_til: Optional[str] = Field(None, alias="gyldig-til")
    rekkefoelge: Optional[float] = None

