import requests
import polars as pl
from bs4 import BeautifulSoup


class BaseScrapper:
    def __init__(self, url: str):
        res = requests.get(url)
        html = res.text
        self.soup = BeautifulSoup(html, "lxml")

    def scrap(self) -> pl.DataFrame:
        raise NotImplementedError
