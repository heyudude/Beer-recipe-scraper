# BeerRecipeScraper

<img alt="beer" src="brewersfriend_ogimage_20180729.jpg" width="800">

Have you ever stood in the beer aisle wondering, “What style am I in the mood for? Do I want a 22-ounce bomber, 
or a 4-pack of 16-ounce cans? Should I try a new brewery’s beer or just grab one of my go-tos?”

With so many options available for craft lovers, the easiest way to choose a brew is by style. 
However, knowing a beer’s vital stats can help your decision-making process ‒ specifically, 
a beer’s alcohol by volume (ABV), international bittering units (IBU), 
standard reference method (SRM) and, sometime (but not always), original gravity (OG).


* **ABV**: Technically, alcohol by volume is defined as a standard measure of how much alcohol is contained in a given volume 
  of an alcoholic beverage. It is defined as the number of milliliters (mL) of pure ethanol present in 100 mL of solution at 20°C (68°F). 
  The number of milliliters of pure ethanol is the mass of the ethanol divided by its density at 20 °C. 
  The higher the ABV, the boozier a beer will be in its aroma and flavor.
  
* **IBU**: IBUs measure the parts per million of isohumulone found in a beer. 
  Isohumulone is the acid found in hops that gives beer its distinct bitterness. 
  Though the IBU scale can be used as a general guideline for taste, with lower IBUs corresponding to less bitterness and vice versa, 
  it's important to note that malt and other flavors can mask the taste of bitterness in beer.
  
* **SRM:** While not quite as recognizable and widespread as alcohol by volume and international bittering units,
  SRM or Standard Reference Method is about as close as the beer world comes to a unified way of gauging color.
  
* **OG:** Though a wee bit more granular than, say, the easily understood numbers of ABV, IBU and SRM, 
  original gravity is defined as the relative density of the wort – the liquid that will ferment and become beer. 
  That density revolves mostly around the quantity of fermentable sugars in the wort, which are fermented by the yeast 
  and become alcohol. In terms of usefulness, OG is regarded as a guide to the alcoholic strength of the finished beer, 
  but in a more brewer-friendly term than, say, ABV, which is very clear to anyone who wants to purchase any alcoholic beverage.
  

While an immense amount of effort and work went into making beers, 
consumers must be able to glance at a beer’s vital stats and immediately comprehend what they mean – 
and make more informed decisions as a result. 
Thanks to ABV, IBU, SRM and OG, that has never been easier.

**Table of content:**
* [Installation](#installation)
* [Technologies Used](#technologies)
* [Function](#function)
* [License](#license)

### Installation

To run this package follow these instructions:

1. Install the package
```
pip install git+https://github.com/Tsukinome/BeerRecipeScraper
```
2. Import the class
```
from beerscraper import BeerScraper
```
3. Create an object and use the functions
```
scrape = BeerScraper()
test_list = scrape.beer(1, 2)
```

### Function 

beer(int, int)

Scrapes beers of given page interval (start_page; end_page)

### Technologies
For the used packages and technologies view the [requirements.txt](requirements.txt) file.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
