import axios from 'axios';
import * as GrepTypes from './types';

// Eksporter typene videre ut til brukeren
export * from './types';

/**
 * Hovedklassen for å kommunisere med Grep API-et.
 */
export class GrepClient {
    private baseUrl: string;

    constructor(baseUrl: string = "https://data.udir.no/kl06/v201906") {
        this.baseUrl = baseUrl;
    }

    /**
     * Intern hjelper for enkle kall
     */
    private async fetch<T>(path: string): Promise<T> {
        const cleanPath = path.startsWith('/') ? path.substring(1) : path;
        const url = `${this.baseUrl}/${cleanPath}`;

        try {
            const response = await axios.get<T>(url);
            return response.data;
        } catch (error: any) {
            // Vi logger ikke feilen her lenger, for 404 er "forventet" i fallback-logikken
            throw error;
        }
    }

    /**
     * Smart hjelper som prøver primær-sti først (f.eks. LK20),
     * og faller tilbake til sekundær-sti (f.eks. LK06) ved 404.
     */
    private async fetchWithFallback<T1, T2>(
        primaryPath: string, 
        secondaryPath: string
    ): Promise<T1 | T2> {
        try {
            return await this.fetch<T1>(primaryPath);
        } catch (error: any) {
            if (error.response && error.response.status === 404) {
                // Prøv gammel metode
                return await this.fetch<T2>(secondaryPath);
            }
            throw error;
        }
    }

    // ==========================================
    // 1. LÆREPLANER
    // ==========================================

    /**
     * Henter en læreplan. Sjekker først LK20, deretter LK06.
     */
    async getLaereplan(kode: string): Promise<GrepTypes.LaereplanLk20 | GrepTypes.Laereplan> {
        return this.fetchWithFallback<GrepTypes.LaereplanLk20, GrepTypes.Laereplan>(
            `laereplaner-lk20/${kode}`,
            `laereplaner/${kode}`
        );
    }

    // ==========================================
    // 2. KOMPETANSEMÅLSETT
    // ==========================================

    /**
     * Henter et kompetansemålsett. Sjekker først LK20, deretter LK06.
     */
    async getKompetansemaalsett(kode: string): Promise<GrepTypes.KompetansemaalsettLk20 | GrepTypes.Kompetansemaalsett> {
        return this.fetchWithFallback<GrepTypes.KompetansemaalsettLk20, GrepTypes.Kompetansemaalsett>(
            `kompetansemaalsett-lk20/${kode}`,
            `kompetansemaalsett/${kode}`
        );
    }

    // ==========================================
    // 3. KOMPETANSEMÅL (Enkeltmål)
    // ==========================================

    /**
     * Henter et enkelt kompetansemål. Sjekker først LK20, deretter LK06.
     */
    async getKompetansemaal(kode: string): Promise<GrepTypes.KompetansemaalLk20 | GrepTypes.Kompetansemaal> {
        return this.fetchWithFallback<GrepTypes.KompetansemaalLk20, GrepTypes.Kompetansemaal>(
            `kompetansemaal-lk20/${kode}`,
            `kompetansemaal/${kode}`
        );
    }
}
