// test_sdk.ts
import { GrepClient } from './src/index';

async function run() {
    console.log("--- Starter Grep SDK Test ---");
    const grep = new GrepClient();

    try {
        // La oss prøve å hente Matematikk R1 (MAT01-05 er vel grunnskole/felles, la oss prøve en vi vet finnes)
        // Bruk gjerne en kode du vet fungerer, f.eks. MAT01-05 eller NOR01-06
        const kode = "MAT01-05"; 
        console.log(`Henter læreplan for ${kode}...`);

        const plan = await grep.getLaereplan(kode);

        // HER KOMMER MAGIEN:
        // Hvis du bruker VS Code og skriver "plan.", skal du nå få opp forslag!
        console.log(`\n✅ Suksess! Fant plan:`);
        console.log(`Tittel: ${JSON.stringify(plan.tittel)}`);
        console.log(`Grep-type: ${plan['grep-type']}`);
        
        // Sjekk om vi fant kjerneelementer
        if (plan.kjerneelementer && plan.kjerneelementer.length > 0) {
             console.log(`\nFant ${plan.kjerneelementer.length} kjerneelementer.`);
        }

    } catch (e) {
        console.error("❌ Noe gikk galt:", e);
    }
}

run();