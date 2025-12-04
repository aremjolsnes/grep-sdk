using System.Text.Json.Serialization;

namespace Udir.GrepSdk.Models;

// Base interfaces or classes if needed, but for now we'll just use POCOs.

public class Aarstrinn
{
    [JsonPropertyName("id")] public string? Id { get; set; }
    [JsonPropertyName("kode")] public string? Kode { get; set; }
    [JsonPropertyName("uri")] public string? Uri { get; set; }
    [JsonPropertyName("url-data")] public string? UrlData { get; set; }
    [JsonPropertyName("tittel")] public object? Tittel { get; set; } // Using object for flexibility as it can be localized string or simple string
    [JsonPropertyName("grep-type")] public string? GrepType { get; set; }
    [JsonPropertyName("status")] public string? Status { get; set; }
    [JsonPropertyName("sist-endret")] public string? SistEndret { get; set; }
    [JsonPropertyName("numerisk-verdi")] public double? NumeriskVerdi { get; set; }
    [JsonPropertyName("kortform")] public List<object>? Kortform { get; set; }
    [JsonPropertyName("gyldig-fra")] public string? GyldigFra { get; set; }
    [JsonPropertyName("gyldig-til")] public string? GyldigTil { get; set; }
    [JsonPropertyName("rekkefoelge")] public double? Rekkefoelge { get; set; }
    [JsonPropertyName("gyldighet")] public Dictionary<string, object>? Gyldighet { get; set; }
    [JsonPropertyName("label")] public List<object>? Label { get; set; }
}

public class Laereplan
{
    [JsonPropertyName("kode")] public string? Kode { get; set; }
    [JsonPropertyName("uri")] public string? Uri { get; set; }
    [JsonPropertyName("url-data")] public string? UrlData { get; set; }
    [JsonPropertyName("tittel")] public object? Tittel { get; set; }
    [JsonPropertyName("gyldighet")] public Dictionary<string, object>? Gyldighet { get; set; }
    [JsonPropertyName("id")] public string? Id { get; set; }
    [JsonPropertyName("grep-type")] public string? GrepType { get; set; }
    [JsonPropertyName("status")] public string? Status { get; set; }
    [JsonPropertyName("tilhoerende-kompetansemaalsett")] public List<object>? TilhoerendeKompetansemaalsett { get; set; }
    [JsonPropertyName("sist-endret")] public string? SistEndret { get; set; }
    [JsonPropertyName("merkelapper")] public List<object>? Merkelapper { get; set; }
    [JsonPropertyName("programfag-kapittel")] public object? ProgramfagKapittel { get; set; }
    [JsonPropertyName("hovedomraade-kapittel")] public object? HovedomraadeKapittel { get; set; }
    [JsonPropertyName("kompetansemaal-kapittel")] public object? KompetansemaalKapittel { get; set; }
    [JsonPropertyName("fastsettelsesinformasjon")] public object? Fastsettelsesinformasjon { get; set; }
    [JsonPropertyName("fagtype")] public List<object>? Fagtype { get; set; }
    [JsonPropertyName("tilgjengelige-spraak")] public List<object>? TilgjengeligeSpraak { get; set; }
    [JsonPropertyName("opplaeringsnivaa")] public List<object>? Opplaeringsnivaa { get; set; }
    [JsonPropertyName("gyldighetsperiode")] public object? Gyldighetsperiode { get; set; }
    [JsonPropertyName("erstatter")] public List<object>? Erstatter { get; set; }
    [JsonPropertyName("erstattes-av")] public List<object>? ErstattesAv { get; set; }
    [JsonPropertyName("formaal-kapittel")] public object? FormaalKapittel { get; set; }
    [JsonPropertyName("timetall-kapittel")] public object? TimetallKapittel { get; set; }
    [JsonPropertyName("struktur-kapittel")] public object? StrukturKapittel { get; set; }
    [JsonPropertyName("grunnleggende-ferdigheter-kapittel")] public object? GrunnleggendeFerdigheterKapittel { get; set; }
    [JsonPropertyName("vurdering-kapittel")] public object? VurderingKapittel { get; set; }
    [JsonPropertyName("siste-eksamen")] public string? SisteEksamen { get; set; }
    [JsonPropertyName("soekehjelp-navn-motsatt-maalform")] public string? SoekehjelpNavnMotsattMaalform { get; set; }
    [JsonPropertyName("tilleggsopplysninger")] public object? Tilleggsopplysninger { get; set; }
    [JsonPropertyName("label")] public List<object>? Label { get; set; }
}

public class LaereplanLk20
{
    [JsonPropertyName("kode")] public string? Kode { get; set; }
    [JsonPropertyName("uri")] public string? Uri { get; set; }
    [JsonPropertyName("url-data")] public string? UrlData { get; set; }
    [JsonPropertyName("tittel")] public object? Tittel { get; set; }
    [JsonPropertyName("gyldighet")] public Dictionary<string, object>? Gyldighet { get; set; }
    [JsonPropertyName("id")] public string? Id { get; set; }
    [JsonPropertyName("grep-type")] public string? GrepType { get; set; }
    [JsonPropertyName("status")] public string? Status { get; set; }
    [JsonPropertyName("kortform")] public List<object>? Kortform { get; set; }
    [JsonPropertyName("sist-endret")] public string? SistEndret { get; set; }
    [JsonPropertyName("laereplanstruktur")] public object? Laereplanstruktur { get; set; }
    [JsonPropertyName("fastsettelsesinformasjon")] public object? Fastsettelsesinformasjon { get; set; }
    [JsonPropertyName("fagtype")] public List<object>? Fagtype { get; set; }
    [JsonPropertyName("tilgjengelige-spraak")] public List<object>? TilgjengeligeSpraak { get; set; }
    [JsonPropertyName("opplaeringsnivaa")] public List<object>? Opplaeringsnivaa { get; set; }
    [JsonPropertyName("ordforklaringer")] public List<object>? Ordforklaringer { get; set; }
    [JsonPropertyName("gyldighetsperiode")] public object? Gyldighetsperiode { get; set; }
    [JsonPropertyName("erstatter")] public List<object>? Erstatter { get; set; }
    [JsonPropertyName("erstattes-av")] public List<object>? ErstattesAv { get; set; }
    [JsonPropertyName("siste-eksamen")] public string? SisteEksamen { get; set; }
    [JsonPropertyName("merkelapper")] public List<object>? Merkelapper { get; set; }
    [JsonPropertyName("om-faget-kapittel")] public object? OmFagetKapittel { get; set; }
    [JsonPropertyName("kompetansemaal-kapittel")] public object? KompetansemaalKapittel { get; set; }
    [JsonPropertyName("vurderingsordning-kapittel")] public object? VurderingsordningKapittel { get; set; }
    [JsonPropertyName("vurderingsordninger-kapittel")] public object? VurderingsordningerKapittel { get; set; }
    [JsonPropertyName("tilleggsopplysninger")] public List<object>? Tilleggsopplysninger { get; set; }
    [JsonPropertyName("opprinnelige-planer")] public List<object>? OpprinneligePlaner { get; set; }
    [JsonPropertyName("label")] public List<object>? Label { get; set; }
    [JsonPropertyName("tilhoerende-kompetansemaalsett")] public List<object>? TilhoerendeKompetansemaalsett { get; set; }
}

public class Kompetansemaalsett
{
    [JsonPropertyName("id")] public string? Id { get; set; }
    [JsonPropertyName("kode")] public string? Kode { get; set; }
    [JsonPropertyName("uri")] public string? Uri { get; set; }
    [JsonPropertyName("url-data")] public string? UrlData { get; set; }
    [JsonPropertyName("tittel")] public object? Tittel { get; set; }
    [JsonPropertyName("grep-type")] public string? GrepType { get; set; }
    [JsonPropertyName("etter-fag")] public List<object>? EtterFag { get; set; }
    [JsonPropertyName("programfag")] public object? Programfag { get; set; }
    [JsonPropertyName("hovedomraader-i-kontekst-av-kompetansemaalsett")] public List<object>? HovedomraaderIKontekstAvKompetansemaalsett { get; set; }
    [JsonPropertyName("kompetansemaal")] public List<object>? Kompetansemaal { get; set; }
    [JsonPropertyName("tilhoerer-laereplan")] public object? TilhoererLaereplan { get; set; }
    [JsonPropertyName("maal-for-kompetansemaalene-overskrift")] public List<object>? MaalForKompetansemaaleneOverskrift { get; set; }
    [JsonPropertyName("benyttes-paa-aarstrinn")] public List<object>? BenyttesPaaAarstrinn { get; set; }
    [JsonPropertyName("etter-aarstrinn")] public List<object>? EtterAarstrinn { get; set; }
    [JsonPropertyName("gyldighet")] public Dictionary<string, object>? Gyldighet { get; set; }
    [JsonPropertyName("status")] public string? Status { get; set; }
    [JsonPropertyName("rekkefoelge")] public double? Rekkefoelge { get; set; }
    [JsonPropertyName("label")] public List<object>? Label { get; set; }
}

public class KompetansemaalsettLk20
{
    [JsonPropertyName("id")] public string? Id { get; set; }
    [JsonPropertyName("kode")] public string? Kode { get; set; }
    [JsonPropertyName("uri")] public string? Uri { get; set; }
    [JsonPropertyName("url-data")] public string? UrlData { get; set; }
    [JsonPropertyName("tittel")] public object? Tittel { get; set; }
    [JsonPropertyName("kortform")] public List<object>? Kortform { get; set; }
    [JsonPropertyName("grep-type")] public string? GrepType { get; set; }
    [JsonPropertyName("rekkefoelge")] public double? Rekkefoelge { get; set; }
    [JsonPropertyName("forklaring")] public List<object>? Forklaring { get; set; }
    [JsonPropertyName("status")] public string? Status { get; set; }
    [JsonPropertyName("sist-endret")] public string? SistEndret { get; set; }
    [JsonPropertyName("kompetansemaal-overskrift")] public object? KompetansemaalOverskrift { get; set; }
    [JsonPropertyName("kompetansemaal-ingress")] public object? KompetansemaalIngress { get; set; }
    [JsonPropertyName("kompetansemaal")] public List<object>? Kompetansemaal { get; set; }
    [JsonPropertyName("underveisvurdering")] public object? Underveisvurdering { get; set; }
    [JsonPropertyName("standpunktvurdering")] public object? Standpunktvurdering { get; set; }
    [JsonPropertyName("etter-fag")] public List<object>? EtterFag { get; set; }
    [JsonPropertyName("etter-aarstrinn")] public List<object>? EtterAarstrinn { get; set; }
    [JsonPropertyName("benyttes-paa-aarstrinn")] public List<object>? BenyttesPaaAarstrinn { get; set; }
    [JsonPropertyName("tilhoerer-laereplan")] public object? TilhoererLaereplan { get; set; }
    [JsonPropertyName("gyldighet")] public Dictionary<string, object>? Gyldighet { get; set; }
    [JsonPropertyName("label")] public List<object>? Label { get; set; }
}

public class Kompetansemaal
{
    [JsonPropertyName("rekkefoelge")] public double? Rekkefoelge { get; set; }
    [JsonPropertyName("tilhoerer-hovedomraade")] public object? TilhoererHovedomraade { get; set; }
    [JsonPropertyName("kode")] public string? Kode { get; set; }
    [JsonPropertyName("uri")] public string? Uri { get; set; }
    [JsonPropertyName("url-data")] public string? UrlData { get; set; }
    [JsonPropertyName("tittel")] public object? Tittel { get; set; }
    [JsonPropertyName("gyldighet")] public Dictionary<string, object>? Gyldighet { get; set; }
    [JsonPropertyName("id")] public string? Id { get; set; }
    [JsonPropertyName("grep-type")] public string? GrepType { get; set; }
    [JsonPropertyName("status")] public string? Status { get; set; }
    [JsonPropertyName("sist-endret")] public string? SistEndret { get; set; }
    [JsonPropertyName("laereplan-referanser")] public List<object>? LaereplanReferanser { get; set; }
    [JsonPropertyName("label")] public List<object>? Label { get; set; }
}

public class KompetansemaalLk20
{
    [JsonPropertyName("kode")] public string? Kode { get; set; }
    [JsonPropertyName("uri")] public string? Uri { get; set; }
    [JsonPropertyName("url-data")] public string? UrlData { get; set; }
    [JsonPropertyName("tittel")] public object? Tittel { get; set; }
    [JsonPropertyName("gyldighet")] public Dictionary<string, object>? Gyldighet { get; set; }
    [JsonPropertyName("id")] public string? Id { get; set; }
    [JsonPropertyName("grep-type")] public string? GrepType { get; set; }
    [JsonPropertyName("status")] public string? Status { get; set; }
    [JsonPropertyName("rekkefoelge")] public double? Rekkefoelge { get; set; }
    [JsonPropertyName("tilknyttede-tverrfaglige-temaer")] public List<object>? TilknyttedeTverrfagligeTemaer { get; set; }
    [JsonPropertyName("tilknyttede-kjerneelementer")] public List<object>? TilknyttedeKjerneelementer { get; set; }
    [JsonPropertyName("tilknyttede-grunnleggende-ferdigheter")] public List<object>? TilknyttedeGrunnleggendeFerdigheter { get; set; }
    [JsonPropertyName("tilknyttede-verb")] public List<object>? TilknyttedeVerb { get; set; }
    [JsonPropertyName("bygger-paa")] public List<object>? ByggerPaa { get; set; }
    [JsonPropertyName("samme-som")] public List<object>? SammeSom { get; set; }
    [JsonPropertyName("tilhoerer-kompetansemaalsett")] public object? TilhoererKompetansemaalsett { get; set; }
    [JsonPropertyName("tilhoerer-laereplan")] public object? TilhoererLaereplan { get; set; }
    [JsonPropertyName("gjenbruk-av")] public string? GjenbrukAv { get; set; }
    [JsonPropertyName("hentet-fra")] public object? HentetFra { get; set; }
    [JsonPropertyName("forklaring")] public List<object>? Forklaring { get; set; }
    [JsonPropertyName("sist-endret")] public string? SistEndret { get; set; }
    [JsonPropertyName("label")] public List<object>? Label { get; set; }
}
