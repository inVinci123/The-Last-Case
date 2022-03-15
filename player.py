class Player:
    name: str
    score: int
    location = int

    def __init__(self, name, score, location):
        self.name = name
        self.score = score
        self.location = location