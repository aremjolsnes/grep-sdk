/**
 * Element som uttrykker den samlede kompetansen en elev, lærling,  lærekandidat eller deltaker skal ha etter endt opplæring på et gitt nivå/trinn i ett eller flere fag etter Kunnskapsløftet LK20, fagfornyelsen
 * @description (EN) Element that indicates the overall competence a student, apprentice, training candidate or participant must have after completing training at a specified level/year-level in one or more subjects according to the Knowledge promotion (LK20)
 * @see http://psi.udir.no/ontologi/kl06/Laereplan_lk20
 */
export interface Laereplan {

  /**
   * Egenskap for alle typer i Greps datamodell for å angi en unik identifikator i dette navnerommet
   */
  kode: string;

  /**
   * Egenskap for alle elementer for å angi hvilken type element det er i datamodellen til Grep (ontologi), der verdien er en lenke til detaljert informasjon om typen
   */
  'grep-type': string;

  /**
   * Egenskap for flere typer elementer for å gi det en benevnelse eller et navn/etikett
   */
  tittel: string;

  /**
   * Egenskap for "laereplan_lk20" for å angi hvilke kjerneelemeter det har
   */
  kjerneelementer: any[];
}
