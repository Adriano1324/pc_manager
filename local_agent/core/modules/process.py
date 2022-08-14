from datetime import datetime


class Process:
    def __init__(self, name):
        self.start_date = datetime.now()
        self.name = name

    def get_informations(self):
        return f"{self.start_date}"

    def run(self):
        pass
