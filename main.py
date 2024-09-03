from scraper import Scraper
from sheet import Sheet
from config import URL, HEADLESS

def main():
    scraper = Scraper(url=URL, headless=HEADLESS)
    day, exercises = scraper.scrape()
    
    sheet = Sheet()
    sheets = sheet.spreadsheet.worksheets()
    
     # if the day already exists, clear the sheet
    if day in [sheet.title for sheet in sheets]:
        sheet.worksheet = sheet.spreadsheet.worksheet(day)
        sheet.clear_sheet()
    # if the day does not exist, create a new worksheet
    else:
        sheet.create_worksheet(day, rows=len(exercises), cols=4)
    
    sheet.worksheet = sheet.spreadsheet.worksheet(day)
    sheet.update_exercises(exercises)

if __name__ == "__main__":
    main()
