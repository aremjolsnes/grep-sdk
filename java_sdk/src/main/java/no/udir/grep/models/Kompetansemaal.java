package no.udir.grep.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;
import java.util.Map;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Kompetansemaal {
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

    @JsonProperty("laereplan-referanser")
    public List<Object> laereplanReferanser;

    @JsonProperty("rekkefoelge")
    public Double rekkefoelge;

    @JsonProperty("tilhoerer-hovedomraade")
    public Object tilhoererHovedomraade;

    @JsonProperty("gyldighet")
    public Map<String, Object> gyldighet;

    @JsonProperty("status")
    public String status;

    @JsonProperty("sist-endret")
    public String sistEndret;

    @JsonProperty("label")
    public List<Object> label;
}
