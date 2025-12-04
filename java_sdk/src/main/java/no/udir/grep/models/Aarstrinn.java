package no.udir.grep.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;
import java.util.Map;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Aarstrinn {
    @JsonProperty("id")
    public String id;

    @JsonProperty("kode")
    public String kode;

    @JsonProperty("uri")
    public String uri;

    @JsonProperty("url-data")
    public String urlData;

    @JsonProperty("tittel")
    public Object tittel;

    @JsonProperty("grep-type")
    public String grepType;

    @JsonProperty("status")
    public String status;

    @JsonProperty("sist-endret")
    public String sistEndret;

    @JsonProperty("numerisk-verdi")
    public Double numeriskVerdi;

    @JsonProperty("kortform")
    public List<Object> kortform;

    @JsonProperty("gyldig-fra")
    public String gyldigFra;

    @JsonProperty("gyldig-til")
    public String gyldigTil;

    @JsonProperty("rekkefoelge")
    public Double rekkefoelge;

    @JsonProperty("gyldighet")
    public Map<String, Object> gyldighet;

    @JsonProperty("label")
    public List<Object> label;
}
