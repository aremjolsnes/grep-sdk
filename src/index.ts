// src/index.ts

/**
 * Hovedklassen for å kommunisere med Grep API-et.
 */
export class GrepClient {
    constructor() {
        console.log("Grep SDK initialized! 🚀");
    }

    /**
     * Henter en læreplan (Placeholder - implementasjon kommer)
     * @param kode Læreplan-kode (f.eks. MAT01-05)
     */
    async getLaereplan(kode: string): Promise<any> {
        // Her skal logikken komme senere
        return { 
            tittel: "Foreløpig ikke implementert",
            kode: kode
        };
    }
}
