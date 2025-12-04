package no.udir.grep.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;
import java.util.Map;

@JsonIgnoreProperties(ignoreUnknown = true)
public class LaereplanLk20 {
    @JsonProperty("kode")
    public String kode;

    @JsonProperty("uri")
    public String uri;

    @JsonProperty("url-data")
    public String urlData;

    @JsonProperty("tittel")
    public Object tittel;

    @JsonProperty("gyldighet")
    public Map<String, Object> gyldighet;

    @JsonProperty("id")
    public String id;

    @JsonProperty("grep-type")
    public String grepType;

    @JsonProperty("status")
    public String status;

    @JsonProperty("kortform")
    public List<Object> kortform;

    @JsonProperty("sist-endret")
    public String sistEndret;

    @JsonProperty("laereplanstruktur")
    public Object laereplanstruktur;

    @JsonProperty("tilhoerende-kompetansemaalsett")
    public List<Object> tilhoerendeKompetansemaalsett;

    @JsonProperty("fastsettelsesinformasjon")
    public Object fastsettelsesinformasjon;

    @JsonProperty("fagtype")
    public List<Object> fagtype;

    @JsonProperty("tilgjengelige-spraak")
    public List<Object> tilgjengeligeSpraak;

    @JsonProperty("opplaeringsnivaa")
    public List<Object> opplaeringsnivaa;

    @JsonProperty("ordforklaringer")
    public List<Object> ordforklaringer;

    @JsonProperty("gyldighetsperiode")
    public Object gyldighetsperiode;

    @JsonProperty("erstatter")
    public List<Object> erstatter;

    @JsonProperty("erstattes-av")
    public List<Object> erstattesAv;

    @JsonProperty("siste-eksamen")
    public String sisteEksamen;

    @JsonProperty("merkelapper")
    public List<Object> merkelapper;

    @JsonProperty("om-faget-kapittel")
    public Object omFagetKapittel;

    @JsonProperty("kompetansemaal-kapittel")
    public Object kompetansemaalKapittel;

    @JsonProperty("vurderingsordning-kapittel")
    public Object vurderingsordningKapittel;

    @JsonProperty("vurderingsordninger-kapittel")
    public Object vurderingsordningerKapittel;

    @JsonProperty("tilleggsopplysninger")
    public List<Object> tilleggsopplysninger;

    @JsonProperty("opprinnelige-planer")
    public List<Object> opprinneligePlaner;

    @JsonProperty("label")
    public List<Object> label;
}
