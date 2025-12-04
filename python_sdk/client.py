import requests
from typing import TypeVar, Type, Union, Any
from .models import (
    Laereplan, LaereplanLk20, 
    Kompetansemaalsett, KompetansemaalsettLk20,
    Kompetansemaal, KompetansemaalLk20
)

# Generisk type for Pydantic-modeller
T = TypeVar("T")

class GrepClient:
    def __init__(self, base_url: str = "https://data.udir.no/kl06/v201906"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def _fetch(self, path: str, model: Type[T]) -> T:
        """Hjelper for å hente data og validere mot Pydantic-modell."""
        url = f"{self.base_url}/{path}"
        response = self.session.get(url)
        response.raise_for_status() # Kaster feil ved 404/500
        return model(**response.json())

    def _fetch_with_fallback(self, path_primary: str, model_primary: Type[Any], 
                             path_secondary: str, model_secondary: Type[Any]) -> Any:
        """Prøver primær-rute (f.eks LK20), faller tilbake til sekundær (LK06) ved 404."""
        try:
            return self._fetch(path_primary, model_primary)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return self._fetch(path_secondary, model_secondary)
            raise e

    # --- Hovedmetoder ---

    def get_laereplan(self, kode: str) -> Union[LaereplanLk20, Laereplan]:
        """Henter læreplan (LK20 eller LK06)."""
        return self._fetch_with_fallback(
            f"laereplaner-lk20/{kode}", LaereplanLk20,
            f"laereplaner/{kode}", Laereplan
        )

    def get_kompetansemaalsett(self, kode: str) -> Union[KompetansemaalsettLk20, Kompetansemaalsett]:
        """Henter kompetansemålsett."""
        return self._fetch_with_fallback(
            f"kompetansemaalsett-lk20/{kode}", KompetansemaalsettLk20,
            f"kompetansemaalsett/{kode}", Kompetansemaalsett
        )

    def get_kompetansemaal(self, kode: str) -> Union[KompetansemaalLk20, Kompetansemaal]:
        """Henter kompetansemål."""
        return self._fetch_with_fallback(
            f"kompetansemaal-lk20/{kode}", KompetansemaalLk20,
            f"kompetansemaal/{kode}", Kompetansemaal
        )