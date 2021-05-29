import unittest
from models.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_rules__rock_beats_scissors(self):
        self.assertEqual("scissors", self.game.rules["rock"])

    def test_rules__paper_beats_rock(self):
        self.assertEqual("rock", self.game.rules["paper"])        

    def test_rules__scissors_beats_paper(self):
        self.assertEqual("paper", self.game.rules["scissors"])


    def test_method_decide_result_returns_correct_result___rock_wins(self):
        self.assertEqual("rock", self.game.decide_result("rock", "scissors"))

    def test_method_decide_result_returns_correct_result___draw(self):
        self.assertEqual("rock", self.game.decide_result("rock", "rock"))

    def test_method_decide_result_returns_correct_result___rock_loses(self):
        self.assertEqual("paper", self.game.decide_result("rock", "paper"))