# main.py

from scraper import Scraper
from sheet import Sheet
from config import URL, HEADLESS

def main():
    value = Sheet().get_cell("A1")
    print(value)
    # scraper = Scraper(url=URL, headless=HEADLESS)
    # exercises = scraper.scrape()
    # print(exercises)

if __name__ == "__main__":
    main()
