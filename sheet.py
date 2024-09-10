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
        
        # Prepare the headers for the sheet
        headers = ['Exercise', 'Sets', 'Ryan: Weight (kg)', 'Ryan: Reps', 'Jamie: Weight(kg)', 'Jamie: Reps: (TARGET)', 'Jamie Reps: (ACTUAL)', 'Notes']
        
        # Initialize the data list with headers
        data = [headers]

        # Populate the data for each exercise
        for exercise in exercises:
            for i, s in enumerate(exercise.sets):
                # Add exercise name only in the first row of its sets
                name = exercise.name if i == 0 else ''
                # Each set will have the name, number of sets, weight, and reps
                row = [name, i+1, '0', '0', s['weight'], s['reps'], '0', 'MASSIVE GAINS']
                data.append(row)
        
        # Update the worksheet starting from cell A1
        self.worksheet.update('A1', data)
        
        # add formating and colours to the sheet
        self.worksheet.format('A1:H', {'horizontalAlignment': 'CENTER'})
        self.worksheet.format('A1:H1', {'textFormat': {'bold': True}})
        self.worksheet.format('C1:D', {'backgroundColor': {'red': 0.0, 'green': 1.0, 'blue': 0.0}})
        self.worksheet.format('E1:F', {'backgroundColor': {'red': 1.0, 'green': 0.5, 'blue': 0.0}})
        print("Exercises updated successfully.")


    