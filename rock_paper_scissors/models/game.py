from models.player import Player

class Game:

    def __init__(self):
        self.rules = {
            "rock" : "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

    def decide_result(self, player1, player2):
        if player2.choice in self.rules[player1.choice]:
            return player1.choice
        return player2.choice