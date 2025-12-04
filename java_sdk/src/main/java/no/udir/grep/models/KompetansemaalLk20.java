package no.udir.grep.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;
import java.util.Map;

@JsonIgnoreProperties(ignoreUnknown = true)
public class KompetansemaalLk20 {
    @JsonProperty("id")
    public String id;

    @JsonProperty("kode")
    public String kode;

    @JsonProperty("uri")
    public String uri;

    @JsonProperty("tittel")
    public Object tittel;

    @JsonProperty("grep-type")
    public String grepType;

    @JsonProperty("tilhoerer-kompetansemaalsett")
    public Object tilhoererKompetansemaalsett;

    @JsonProperty("gyldighet")
    public Map<String, Object> gyldighet;

    @JsonProperty("status")
    public String status;

    @JsonProperty("rekkefoelge")
    public Double rekkefoelge;

    @JsonProperty("tilknyttede-tverrfaglige-temaer")
    public List<Object> tilknyttedeTverrfagligeTemaer;

    @JsonProperty("tilknyttede-kjerneelementer")
    public List<Object> tilknyttedeKjerneelementer;

    @JsonProperty("tilknyttede-grunnleggende-ferdigheter")
    public List<Object> tilknyttedeGrunnleggendeFerdigheter;

    @JsonProperty("tilknyttede-verb")
    public List<Object> tilknyttedeVerb;

    @JsonProperty("bygger-paa")
    public List<Object> byggerPaa;

    @JsonProperty("samme-som")
    public List<Object> sammeSom;

    @JsonProperty("tilhoerer-laereplan")
    public Object tilhoererLaereplan;

    @JsonProperty("gjenbruk-av")
    public String gjenbrukAv;

    @JsonProperty("hentet-fra")
    public Object hentetFra;

    @JsonProperty("forklaring")
    public List<Object> forklaring;

    @JsonProperty("sist-endret")
    public String sistEndret;

    @JsonProperty("label")
    public List<Object> label;
}
