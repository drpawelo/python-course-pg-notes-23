from card import Card

class Deck:
    suits = ["Diamond", "Club", "Heart", "Spade"]
    ranks  = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    def __init__(self):
        self.cards = self.create_new_cards()
    
    def create_new_cards(self):
        new_cards = []
        for suit in self.suits:
            for rank in self.ranks:
                new_cards.append( Card(suit, rank))
        return new_cards
    
    def get_a_card(self):
        return self.cards.pop()
    
    # great suggestion during the lecture! I'm adding this, It's used by Table
    def shuffle_cards(self):
        import random
        random.shuffle(self.cards)

    
