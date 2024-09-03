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
    
    def get_worksheet(self, title=None):
        return self.worksheet
    
    def clear_sheet(self):
        self.worksheet.clear()
        print("Worksheet cleared successfully.")
        
    def get_all_values(self):
        return self.worksheet.get_all_values()
    
    def create_worksheet(self, title, rows=1, cols=1):
        self.spreadsheet.add_worksheet(title, rows, cols)
        print(f"Worksheet '{title}' created successfully.")
    
    def update_exercises(self, exercises):
        worksheet = self.get_worksheet()

        # Convert exercises to a list of lists
        data = []
        for exercise in exercises:
            data.append([exercise.get_name(), exercise.get_set_number()])
        
       # Update the worksheet with the exercise data
       
        worksheet.update('A1', [['Exercise', 'Number of Sets', 'Ryan', 'Jamie']])
        worksheet.update('A2', data)
        
        print("Exercises updated successfully.")

