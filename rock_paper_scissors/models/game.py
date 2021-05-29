import random
from models.player import Player

class Game:

    def decide_result(self, player1, player2):

        rules = {
            "rock" : "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if player1.choice == player2.choice:
            return None
        if player2.choice in rules[player1.choice]:
            return player1.choice
        return player2.choice

    def decide_vs_cpu(self, player1):

        cpu_options = ["rock", "paper", "scissors"]
        cpu_player = Player("cpu", random.choice(cpu_options))
        self.decide_result(player1, cpu_player)