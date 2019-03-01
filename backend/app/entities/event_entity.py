class EventEntity:
    def __init__(self, title, description, start_date, end_date, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
