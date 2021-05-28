import pandas as pd
from Beer.beerscraper import BeerScraper

def test_shape():
    scraper = BeerScraper()
    assert scraper.beer(1,1) == 20

def test_scrape():
    scraper = BeerScraper()
    df = scraper.beer(1,1)
    assert type(df) == pd.DataFrame
