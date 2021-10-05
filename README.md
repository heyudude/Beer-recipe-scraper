# Beer Scraper

**Table of content:**
* [About](#about)
* [Installation](#installation)
* [Technologies Used](#technologies)
* [Function](#function)
* [License](#license)

### About

This is the first part of the capstone project at Turing College. The goal of the project is to set up a complete machine learning pipeline. The following scrapes the data from https://www.brewersfriend.com/ later used for machine learning.
Brewer's Friend is a set of tools and homebrewing information to help you brew beer.  
Knowing a beer’s vital stats can help your decision-making process ‒ specifically, 
a beer’s alcohol by volume (ABV), international bittering units (IBU), 
standard reference method (SRM), and sometimes (but not always), original gravity (OG) and final gravity (FG).

* **ABV**: Technically, alcohol by volume is defined as a standard measure of how much alcohol is contained in a given volume of an alcoholic beverage. It is defined as the number of milliliters (mL) of pure ethanol present in 100 mL of solution at 20°C (68°F).
  The higher the ABV, the boozier a beer will be in its aroma and flavor.
  
* **IBU**: IBUs measure the parts per million of isohumulone found in a beer. 
  Isohumulone is the acid found in hops that gives beer its distinct bitterness. 
  Though the IBU scale can be used as a general guideline for taste, with lower 
  IBUs corresponding to less bitterness and vice versa, 
  it's important to note that malt and other flavors can mask the taste of bitterness in beer.
  
* **SRM:** While not quite as recognizable and widespread as alcohol by volume and international bittering units,
  SRM or Standard Reference Method is about as close as the beer world comes to a unified way of gauging color.
  
* **OG:** Though a wee bit more granular than, say, the easily understood numbers of ABV, IBU, and SRM, 
  original gravity is defined as the relative density of the wort – the liquid that will ferment and become beer. 
  That density revolves mostly around the quantity of fermentable sugars in the wort, which is fermented by the yeast and become alcohol. In terms of usefulness, OG is regarded as a guide to the alcoholic strength of the finished beer, 
  but in a more brewer-friendly term.
  
* **FG:** If the fermentation is finished, the specific gravity is called the final gravity (abbreviated FG). 
  For example, for a typical strength beer, OG could be 1.050 and FG could be 1.010.
  
### Installation

To run this package follow these instructions:

1. Install the package
```python
pip install git+https://github.com/Tsukinome/Beer-recipe-scraper
```
2. Import the class
```python
from Beer.beerscraper import BeerScraper
```
3. Create an object and use the functions
```python
scrape = BeerScraper()
test_list = scrape.beer(1, 2)
```
### Function 

```python
beer()
```
Scrapes beers of given page interval (start_page: int, end_page: int)

### Technologies
For the used packages and technologies view the [requirements.txt](requirements.txt) file.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
