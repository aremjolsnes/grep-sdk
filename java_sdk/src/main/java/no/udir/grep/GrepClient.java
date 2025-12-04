package no.udir.grep;

import com.fasterxml.jackson.databind.ObjectMapper;
import no.udir.grep.models.*;
import okhttp3.*;
import java.io.IOException;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionException;

public class GrepClient {
    private final OkHttpClient httpClient;
    private final String baseUrl;
    private final ObjectMapper objectMapper;

    public GrepClient() {
        this("https://data.udir.no/kl06/v201906");
    }

    public GrepClient(String baseUrl) {
        this.baseUrl = baseUrl.endsWith("/") ? baseUrl.substring(0, baseUrl.length() - 1) : baseUrl;
        this.httpClient = new OkHttpClient();
        this.objectMapper = new ObjectMapper();
    }

    private <T> CompletableFuture<T> fetch(String path, Class<T> responseType) {
        String url = baseUrl + "/" + path;
        Request request = new Request.Builder()
                .url(url)
                .build();

        CompletableFuture<T> future = new CompletableFuture<>();

        httpClient.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                future.completeExceptionally(e);
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                try (ResponseBody body = response.body()) {
                    if (response.code() == 404) {
                        future.completeExceptionally(
                                new CompletionException(new NotFoundException("Not Found: " + url)));
                        return;
                    }
                    if (!response.isSuccessful()) {
                        future.completeExceptionally(new IOException("HTTP Error: " + response.code()));
                        return;
                    }
                    if (body == null) {
                        future.completeExceptionally(new IOException("Empty response body"));
                        return;
                    }
                    try {
                        T result = objectMapper.readValue(body.string(), responseType);
                        future.complete(result);
                    } catch (IOException e) {
                        future.completeExceptionally(e);
                    }
                }
            }
        });

        return future;
    }

    private <T1, T2> CompletableFuture<Object> fetchWithFallback(String primaryPath, Class<T1> primaryType,
            String secondaryPath,
            Class<T2> secondaryType) {
        return fetch(primaryPath, primaryType)
                .handle((result, ex) -> {
                    if (ex == null) {
                        return CompletableFuture.completedFuture((Object) result);
                    }
                    if (ex instanceof CompletionException && ex.getCause() instanceof NotFoundException) {
                        return fetch(secondaryPath, secondaryType).thenApply(r -> (Object) r);
                    }
                    if (ex instanceof NotFoundException) {
                        return fetch(secondaryPath, secondaryType).thenApply(r -> (Object) r);
                    }

                    CompletableFuture<Object> failed = new CompletableFuture<>();
                    failed.completeExceptionally(ex);
                    return failed;
                })
                .thenCompose(x -> x);
    }

    // ==========================================
    // 1. LÆREPLANER
    // ==========================================

    public CompletableFuture<Object> getLaereplan(String kode) {
        return fetchWithFallback(
                "laereplaner-lk20/" + kode, LaereplanLk20.class,
                "laereplaner/" + kode, Laereplan.class).thenApply(obj -> obj);
    }

    // ==========================================
    // 2. KOMPETANSEMÅLSETT
    // ==========================================

    public CompletableFuture<Object> getKompetansemaalsett(String kode) {
        return fetchWithFallback(
                "kompetansemaalsett-lk20/" + kode, KompetansemaalsettLk20.class,
                "kompetansemaalsett/" + kode, Kompetansemaalsett.class).thenApply(obj -> obj);
    }

    // ==========================================
    // 3. KOMPETANSEMÅL (Enkeltmål)
    // ==========================================

    public CompletableFuture<Object> getKompetansemaal(String kode) {
        return fetchWithFallback(
                "kompetansemaal-lk20/" + kode, KompetansemaalLk20.class,
                "kompetansemaal/" + kode, Kompetansemaal.class).thenApply(obj -> obj);
    }

    public static class NotFoundException extends RuntimeException {
        private static final long serialVersionUID = 1L;

        public NotFoundException(String message) {
            super(message);
        }
    }
}
