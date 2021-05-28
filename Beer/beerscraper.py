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

        dicts = []
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

            beer_dict = {}
            recipe = []

            for item in soup.find_all('div', class_='forminput'):
                recipe.append(item)
            recl = str(recipe)

            try:
                title = recl[recl.index('Title:') + 7: recl.index("Author:") - 4]
                beer_dict['title'] = title
            except:
                pass

            try:
                style = recl[recl.index('Style Name:') + 12: recl.index('Boil Time:') - 2]
                beer_dict['style'] = style
            except:
                pass

            try:

                stats = recl[recl.index('STATS:') + 8: recl.index('FERMENTABLES') - 4]
                stats = stats.replace('\r\n', ',').split(',')

                def list_to_dict(stats):
                    return dict(map(lambda s: s.split(':'), stats))

                stats_dict = list_to_dict(stats)
            except:
                pass

            try:
                co2 = recl[recl.index('CO2 Level'): recl.index('TARGET WATER') - 4]
                beer_dict['co2'] = co2
            except:
                pass

            try:
                beer_dict.update(stats_dict)
            except:
                pass


            print(f'getting row {row}')
            dicts.append(beer_dict)


        df = pd.DataFrame.from_dict(dicts)
        df = df.transpose()

        return df






