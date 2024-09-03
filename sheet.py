import gspread
from config import SPREADSHEET, SERVICE_ACCOUNT

class Sheet:
    def __init__(self, filepath=SERVICE_ACCOUNT, spreadsheet=SPREADSHEET):
        self.filepath = filepath
        self.spreadsheet_name = spreadsheet
        self.gc = gspread.service_account(filename=self.filepath)
        self.spreadsheet = self.gc.open(self.spreadsheet_name)
        self.worksheet = None
    
    def clear_sheet(self):
        if self.worksheet:
            self.worksheet.clear()
            print("Worksheet cleared successfully.")
        else:
            print("No worksheet selected.")
        
    def create_worksheet(self, title, rows=1, cols=1):
        self.spreadsheet.add_worksheet(title, rows, cols)
        print(f"Worksheet '{title}' created successfully.")
    
    def update_exercises(self, exercises):
        if not self.worksheet:
            print("No worksheet selected.")
            return
        
        data = [[exercise.name, len(exercise.sets)] for exercise in exercises]
        self.worksheet.update('A1', [['Exercise', 'Number of Sets', 'Ryan', 'Jamie']])
        self.worksheet.update('A2', data)
        print("Exercises updated successfully.")
