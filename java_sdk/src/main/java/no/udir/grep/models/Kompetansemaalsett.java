package no.udir.grep.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;
import java.util.Map;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Kompetansemaalsett {
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

    @JsonProperty("etter-fag")
    public List<Object> etterFag;

    @JsonProperty("programfag")
    public Object programfag;

    @JsonProperty("hovedomraader-i-kontekst-av-kompetansemaalsett")
    public List<Object> hovedomraaderIKontekstAvKompetansemaalsett;

    @JsonProperty("maal-for-kompetansemaalene-overskrift")
    public List<Object> maalForKompetansemaaleneOverskrift;

    @JsonProperty("benyttes-paa-aarstrinn")
    public List<Object> benyttesPaaAarstrinn;

    @JsonProperty("etter-aarstrinn")
    public List<Object> etterAarstrinn;

    @JsonProperty("gyldighet")
    public Map<String, Object> gyldighet;

    @JsonProperty("status")
    public String status;

    @JsonProperty("rekkefoelge")
    public Double rekkefoelge;

    @JsonProperty("label")
    public List<Object> label;
}
