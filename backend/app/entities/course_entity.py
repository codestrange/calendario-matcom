class CourseEntity:
    def __init__(self, name, year, freq, sem, id=None):
        self.id = id
        self.name = name
        self.year = year
        self.freq = freq
        self.sem = sem
