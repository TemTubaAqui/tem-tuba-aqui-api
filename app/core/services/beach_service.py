from typing import Dict, Tuple, Type

from .scrappers import BaseScrapper, ULScrapper

scrap_map: Dict[Tuple[str, str], Tuple[str, Type[BaseScrapper]]] = {
    ("BR", "PE"): (
        "https://pt.wikipedia.org/wiki/Lista_de_praias_de_Pernambuco",
        ULScrapper,
    )
}


class BeachService:
    def get_beaches(self, country: str, state: str):
        config = scrap_map.get((country, state))
        assert config, f"Scrapper not found for ({country}, {state})"
        url, scrapper = config
        df = scrapper(url).scrap()
        print(df)
