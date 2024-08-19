from db.connect import DB


class Teachers(DB):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

class Subjects(DB):
    def __init__(self , **kwargs):
        self.kwargs = kwargs

class Groups(DB):
    def __init__(self , **kwargs):
        self.kwargs = kwargs

