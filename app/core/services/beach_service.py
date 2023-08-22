from typing import Dict, Tuple, Type

import polars as pl
from django.db import transaction

from app.core.models import Beach, BeachUpdateTask

from .scrappers import BaseScrapper, ULScrapper

scrap_map: Dict[Tuple[str, str], Tuple[str, Type[BaseScrapper]]] = {
    ("BR", "PE"): (
        "https://pt.wikipedia.org/wiki/Lista_de_praias_de_Pernambuco",
        ULScrapper,
    )
}


class BeachService:
    def _get_df(self):
        df: pl.DataFrame = None
        for (country, state), (url, scrapper) in scrap_map.items():
            _df = scrapper(url).scrap()
            _df = _df.with_columns(
                pl.lit(country).alias("country"),
                pl.lit(state).alias("state"),
                pl.lit(0).alias("latitude"),
                pl.lit(0).alias("longitude"),
            )

            if df is None:
                df = _df
            else:
                df = df.vstack(_df)

        return df

    def _save(self, df: pl.DataFrame):
        Beach.objects.all().delete()
        Beach.objects.bulk_create(
            Beach(
                country=row["country"],
                state=row["state"],
                city=row["city"],
                name=row["beach"],
                latitude=row["latitude"],
                longitude=row["longitude"],
            )
            for row in df.to_dicts()
        )

    @transaction.atomic
    def _run(self):
        df = self._get_df()
        self._save(df)

    def execute(self, task: BeachUpdateTask):
        with task.run():
            self._run()
