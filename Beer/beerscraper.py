import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
import time
import random

class BeerScraper:
    """
    A scraper class for beer brewing parameters
        ...
        Methods
        -------
        beer()
    """

    @staticmethod
    def beer(start: int, stop: int):
        """
        Scrapes https://www.brewersfriend.com/ when the interval of pages is given

        :param start: start page for scraping
        :param stop: last page for scraping
        :return: DataFrame
        """

        OG, FG, ABV, SMR, IBU, pH, type = ([] for i in range(7))
        link_dfs = []
        for i in range(start, stop + 1):
            ua = UserAgent()
            user_agent = {'User-agent': ua.random}
            if i == 1:
                page_num = ""
            else:
                page_num = f"page/{i}"
            url_links = f'https://www.brewersfriend.com/homebrew-recipes/{page_num}'
            response_url = requests.get(url_links, headers=user_agent)
            page_url = response_url.text
            soup_url = BeautifulSoup(page_url, 'lxml')

            values = []
            titles = []

            for r_title in soup_url.find_all(class_='recipetitle'):
                r_title = r_title.text
                titles.append(r_title)
            for a in soup_url.find_all('a', class_='recipetitle', href=True):
                value = a['href']
                values.append(value)

            link_dict = dict(zip(titles, values))

            link_df = pd.DataFrame(link_dict, index=['beer']).T
            link_dfs.append(link_df)

        all_links = pd.concat(link_dfs)

        for row in range(len(all_links)):
            time.sleep(.4 + 2.2 * random.random())
            req_headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.8',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
            }
            url = f'https://www.brewersfriend.com{all_links.beer[row]}'
            response = requests.get(url, headers=req_headers)
            if response.status_code != 200:
                print(f'#{row} unresponsive')
                continue
            page = response.text
            soup = BeautifulSoup(page, 'lxml')

            for item in soup.find_all('span', itemprop="recipeCategory"):
                types = getattr(item.find("a"),'text', None)
                type.append(types)

            for item in soup.find_all('div', class_='viewrecipe'):

                OGs = item.find("div", class_='value ogBatch').text.strip()
                OG.append(OGs)

                FGs = item.find("div", class_='value fgBatch').text.strip()
                FG.append(FGs)

                ABVs = item.find("div", class_='value abvMin').text.strip()
                ABV.append(ABVs)

                IBUs = item.find("div", class_='value ibuMin').text.strip()
                IBU.append(IBUs)

                SMRs = item.find("div", class_='value srmMin').text.strip()
                SMR.append(SMRs)

                pHs = item.find("div", class_='value phMin').text.strip()
                pH.append(pHs)

            print(f'getting row {row}')

        dict_ = {
            "OG": OG,
            "FG": FG,
            "ABV": ABV,
            "SMR": SMR,
            "pH": pH,
            "IBU": IBU,
            "type": type
        }

        df = pd.DataFrame.from_dict(dict_, orient='index')
        df = df.transpose()
        df.to_csv('scraped_data.csv', index=False)

        return df
