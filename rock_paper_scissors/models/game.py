class Game:

    def __init__(self):
        self.rules = {
            "rock" : "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

    # def get_preferred_option(task1, task2):
    # if task2.description in task1.lookup[task1.description]:
    #     return task1.description
    # return task2.description

    def decide_result(self, player1_choice, player2_choice):
        if player2_choice in self.rules[player1_choice]:
            return player1_choice
        return player2_choice