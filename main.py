# main.py

from scraper import Scraper
from sheet import Sheet
from config import URL, HEADLESS

def main():
    scraper = Scraper(url=URL, headless=HEADLESS)
    data = scraper.scrape()
    day = data[0]
    exercises = data[1]
    sheet = Sheet()
    sheet.create_worksheet(day, rows=len(exercises), cols=4)
    # select the newly created worksheet
    sheet.worksheet = sheet.spreadsheet.worksheet(day)
    sheet.clear_sheet()
    sheet.update_exercises(exercises)

if __name__ == "__main__":
    main()
