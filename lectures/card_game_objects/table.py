from player import Player
from card import Card
from deck import Deck

class Table:
    def __init__(self, players_names ):
        self.players = self.create_players_from_names(players_names)
        self.deck = Deck()
        self.deck.shuffle_cards(); # shuffle new deck once it's created!
    
    def create_players_from_names(self, names):
        new_players = []
        for name in names:
            new_players.append( Player(name) ) 
        return new_players
    
    def play_the_game(self):
        print("start the game")
        self.deal_everyone_a_card()
        winner = self.who_has_the_highest_first_card()
        print(f"winner is {winner.name} with card {winner.cards[0].as_string()}")

    def deal_everyone_a_card(self):
        for player in self.players:
            a_card = self.deck.get_a_card()
            player.receive_a_card(a_card)
            print(f"{player.name} was dealt {a_card.as_string()}")
            # I forgot to mention this furing the lecture: in objects you can use dot notation like this:
            # someobject.somevariable  for example: player1.name        
            
    def who_has_the_highest_first_card(self): 
        winner = self.players[0]
        for player in self.players:
            if self.which_card_is_higher(winner.cards[0], player.cards[0]) == player.cards[0]:
                winner = player
        return winner
    
    def which_card_is_higher(self, card1, card2):
        if Deck.ranks.index(card1.rank) > Deck.ranks.index(card2.rank):
            return card1
        elif Deck.ranks.index(card1.rank) < Deck.ranks.index(card2.rank):
            return card2
        else:
            if Deck.suits.index(card1.suit) >= Deck.suits.index(card2.suit):
                return card1
            else:
                return card2

