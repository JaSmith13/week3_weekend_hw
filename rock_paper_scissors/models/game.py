
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