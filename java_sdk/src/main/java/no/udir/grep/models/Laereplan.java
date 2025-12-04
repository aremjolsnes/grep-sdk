package no.udir.grep.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;
import java.util.Map;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Laereplan {
    @JsonProperty("kode")
    public String kode;

    @JsonProperty("uri")
    public String uri;

    @JsonProperty("url-data")
    public String urlData;

    @JsonProperty("tittel")
    public Object tittel; // String or Map for localization

    @JsonProperty("gyldighet")
    public Map<String, Object> gyldighet;

    @JsonProperty("id")
    public String id;

    @JsonProperty("grep-type")
    public String grepType;

    @JsonProperty("status")
    public String status;

    @JsonProperty("tilhoerende-kompetansemaalsett")
    public List<Object> tilhoerendeKompetansemaalsett;

    @JsonProperty("sist-endret")
    public String sistEndret;

    @JsonProperty("merkelapper")
    public List<Object> merkelapper;

    @JsonProperty("programfag-kapittel")
    public Object programfagKapittel;

    @JsonProperty("hovedomraade-kapittel")
    public Object hovedomraadeKapittel;

    @JsonProperty("kompetansemaal-kapittel")
    public Object kompetansemaalKapittel;

    @JsonProperty("fastsettelsesinformasjon")
    public Object fastsettelsesinformasjon;

    @JsonProperty("fagtype")
    public List<Object> fagtype;

    @JsonProperty("tilgjengelige-spraak")
    public List<Object> tilgjengeligeSpraak;

    @JsonProperty("opplaeringsnivaa")
    public List<Object> opplaeringsnivaa;

    @JsonProperty("gyldighetsperiode")
    public Object gyldighetsperiode;

    @JsonProperty("erstatter")
    public List<Object> erstatter;

    @JsonProperty("erstattes-av")
    public List<Object> erstattesAv;

    @JsonProperty("formaal-kapittel")
    public Object formaalKapittel;

    @JsonProperty("timetall-kapittel")
    public Object timetallKapittel;

    @JsonProperty("struktur-kapittel")
    public Object strukturKapittel;

    @JsonProperty("grunnleggende-ferdigheter-kapittel")
    public Object grunnleggendeFerdigheterKapittel;

    @JsonProperty("vurdering-kapittel")
    public Object vurderingKapittel;

    @JsonProperty("siste-eksamen")
    public String sisteEksamen;

    @JsonProperty("soekehjelp-navn-motsatt-maalform")
    public String soekehjelpNavnMotsattMaalform;

    @JsonProperty("tilleggsopplysninger")
    public Object tilleggsopplysninger;

    @JsonProperty("label")
    public List<Object> label;
}
