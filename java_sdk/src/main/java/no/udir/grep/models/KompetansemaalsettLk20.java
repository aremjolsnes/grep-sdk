package no.udir.grep.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;
import java.util.Map;

@JsonIgnoreProperties(ignoreUnknown = true)
public class KompetansemaalsettLk20 {
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

    @JsonProperty("kompetansemaal")
    public List<Object> kompetansemaal;

    @JsonProperty("tilhoerer-laereplan")
    public Object tilhoererLaereplan;

    @JsonProperty("kortform")
    public List<Object> kortform;

    @JsonProperty("rekkefoelge")
    public Double rekkefoelge;

    @JsonProperty("forklaring")
    public List<Object> forklaring;

    @JsonProperty("status")
    public String status;

    @JsonProperty("sist-endret")
    public String sistEndret;

    @JsonProperty("kompetansemaal-overskrift")
    public Object kompetansemaalOverskrift;

    @JsonProperty("kompetansemaal-ingress")
    public Object kompetansemaalIngress;

    @JsonProperty("underveisvurdering")
    public Object underveisvurdering;

    @JsonProperty("standpunktvurdering")
    public Object standpunktvurdering;

    @JsonProperty("etter-fag")
    public List<Object> etterFag;

    @JsonProperty("etter-aarstrinn")
    public List<Object> etterAarstrinn;

    @JsonProperty("benyttes-paa-aarstrinn")
    public List<Object> benyttesPaaAarstrinn;

    @JsonProperty("gyldighet")
    public Map<String, Object> gyldighet;

    @JsonProperty("label")
    public List<Object> label;
}
