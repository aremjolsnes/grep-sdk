using System.Net.Http.Json;
using System.Text.Json;
using Udir.GrepSdk.Models;

namespace Udir.GrepSdk;

public class GrepClient
{
    private readonly HttpClient _httpClient;
    private readonly string _baseUrl;

    public GrepClient(string baseUrl = "https://data.udir.no/kl06/v201906")
    {
        _baseUrl = baseUrl.TrimEnd('/');
        _httpClient = new HttpClient();
    }

    public GrepClient(HttpClient httpClient, string baseUrl = "https://data.udir.no/kl06/v201906")
    {
        _baseUrl = baseUrl.TrimEnd('/');
        _httpClient = httpClient;
    }

    private async Task<T> FetchAsync<T>(string path)
    {
        var url = $"{_baseUrl}/{path}";
        var response = await _httpClient.GetAsync(url);
        response.EnsureSuccessStatusCode();
        
        return await response.Content.ReadFromJsonAsync<T>() 
               ?? throw new InvalidOperationException("Failed to deserialize response.");
    }

    private async Task<object> FetchWithFallbackAsync<TPrimary, TSecondary>(
        string primaryPath, 
        string secondaryPath)
    {
        try
        {
            return await FetchAsync<TPrimary>(primaryPath);
        }
        catch (HttpRequestException ex) when (ex.StatusCode == System.Net.HttpStatusCode.NotFound)
        {
            return await FetchAsync<TSecondary>(secondaryPath);
        }
    }

    // ==========================================
    // 1. LÆREPLANER
    // ==========================================

    public async Task<object> GetLaereplanAsync(string kode)
    {
        return await FetchWithFallbackAsync<LaereplanLk20, Laereplan>(
            $"laereplaner-lk20/{kode}",
            $"laereplaner/{kode}"
        );
    }

    // ==========================================
    // 2. KOMPETANSEMÅLSETT
    // ==========================================

    public async Task<object> GetKompetansemaalsettAsync(string kode)
    {
        return await FetchWithFallbackAsync<KompetansemaalsettLk20, Kompetansemaalsett>(
            $"kompetansemaalsett-lk20/{kode}",
            $"kompetansemaalsett/{kode}"
        );
    }

    // ==========================================
    // 3. KOMPETANSEMÅL (Enkeltmål)
    // ==========================================

    public async Task<object> GetKompetansemaalAsync(string kode)
    {
        return await FetchWithFallbackAsync<KompetansemaalLk20, Kompetansemaal>(
            $"kompetansemaal-lk20/{kode}",
            $"kompetansemaal/{kode}"
        );
    }
}
