import gspread
from config import SPREADSHEET, SERVICE_ACCOUNT

# This class is responsible for interacting with the Google Sheets API
# It uses the gspread library to interact with Google Sheets
# The class is initialized with a filepath, spreadsheet name, and worksheet index
# The get_cell method retrieves the value of a cell in the worksheet

class Sheet:
    def __init__(self, filepath=SERVICE_ACCOUNT, spreadsheet=SPREADSHEET, worksheet_index=0):
        self.filepath = filepath
        self.spreadsheet = spreadsheet
        self.worksheet = worksheet_index
        self.gc = gspread.service_account(filename=self.filepath)
        self.spreadsheet = self.gc.open(self.spreadsheet)
        self.worksheet = self.spreadsheet.get_worksheet(self.worksheet)
        
    def get_sreadsheet(self):
        return self.spreadsheet
    
    def get_worksheet(self):
        return self.worksheet
    
    def get_cell(self, cell):
        return self.worksheet.acell(cell).value
    
    

