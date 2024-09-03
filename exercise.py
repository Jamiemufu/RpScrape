class Exercise:
    def __init__(self, name=""):
        self.name = name
        self.sets = []

    def add_set(self, weight, reps):
        self.sets.append({"weight": weight, "reps": reps})

    def __repr__(self):
        return f"Exercise(name={self.name}, sets={self.sets})"
