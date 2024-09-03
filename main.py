from scraper import Scraper
from sheet import Sheet
from config import URL, HEADLESS, USER_PROFILE

def main():
    scraper = Scraper(url=URL, headless=HEADLESS, user_profile=USER_PROFILE)
    day, exercises = scraper.scrape()
    
    sheet = Sheet()
    sheets = sheet.spreadsheet.worksheets()
    
     # if the day already exists, clear the sheet
    if day in [sheet.title for sheet in sheets]:
        print(f"Worksheet '{day}' already exists.")
        return
    # if the day does not exist, create a new worksheet
    else:
        sheet.create_worksheet(day, rows=len(exercises), cols=4)
        sheet.worksheet = sheet.spreadsheet.worksheet(day)
        sheet.update_exercises(exercises)

if __name__ == "__main__":
    main()
