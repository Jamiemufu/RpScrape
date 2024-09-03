
# EXAMPLE
# Exercise(name=Dumbbell Pullover, sets=[{'weight': '29.75', 'reps': '9'}, {'weight': '29.75', 'reps': '8'}])

class Exercise:
    def __init__(self, name=""):
        self.name = name
        self.sets = []

    def add_set(self, weight, reps):
        self.sets.append({"weight": weight, "reps": reps})

    def __repr__(self):
        return f"Exercise(name={self.name}, sets={self.sets})"

