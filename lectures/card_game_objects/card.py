class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def as_string(self):
        return f"{self.rank} or {self.suit}s"