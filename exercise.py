# exercise.py

class Exercise:
    def __init__(self, name=""):
        self.name = name
        self.sets = []

    def add_set(self, weight, reps):
        self.sets.append({"weight": weight, "reps": reps})
        
    def set_name(self, name):
        self.name = name

    def __repr__(self):
        return f"Exercise(name={self.name}, sets={self.sets})"
    
    def get_name(self):
        return self.name
    
    def get_sets(self):
        return self.sets
    
    def get_set_number(self):
        return len(self.sets)
