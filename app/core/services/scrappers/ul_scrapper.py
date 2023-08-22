from typing import List, Tuple

import polars as pl

from .base import BaseScrapper

Group = Tuple[str, List[str]]


class ULScrapper(BaseScrapper):
    def _get_groups(self) -> List[Group]:
        tags = self.soup.select(f".mw-parser-output > *:is(h2, ul)")

        grouped = []
        group: Group = None
        for tag in tags:
            if tag.name == "h2":
                if tag.select_one(".mw-headline").get("id") == "Galeria":
                    break

                city = tag.select(".mw-headline")
                assert city, "City not found"
                city = city[0].text
                if not group:
                    group = (city, [])
                else:
                    grouped.append(group)
                    group = (city, [])
            else:
                beaches = tag.select("li")
                beaches = [beach.text for beach in beaches]
                group[1].extend(beaches)

        grouped.append(group)
        return grouped

    def _get_df(self, groups: List[Group]) -> pl.DataFrame:
        data = []

        for city, beaches in groups:
            for beach in beaches:
                data.append({"city": city, "beach": beach})

        return pl.DataFrame(data)

    def scrap(self) -> pl.DataFrame:
        groups = self._get_groups()
        return self._get_df(groups)
