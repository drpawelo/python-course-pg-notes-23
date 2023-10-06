class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        
    def receive_a_card(self, card):
        self.cards.append(card)