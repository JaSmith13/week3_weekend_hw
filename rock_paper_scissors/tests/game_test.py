import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.player1 = Player("Jack", "paper")
        self.player2 = Player("Meg", "rock")

    # method tests    
    def test_method_can_take_player_choice(self):       
        self.assertEqual("paper", self.game.decide_result(self.player1, self.player2))