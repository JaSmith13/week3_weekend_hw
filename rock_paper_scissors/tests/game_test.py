import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.player1 = Player("Jack", "paper")
        self.player2 = Player("Meg", "rock")
        
    #attribute tests 
    def test_rules__rock_beats_scissors(self):
        self.assertEqual("scissors", self.game.rules["rock"])

    def test_rules__paper_beats_rock(self):
        self.assertEqual("rock", self.game.rules["paper"])        

    def test_rules__scissors_beats_paper(self):
        self.assertEqual("paper", self.game.rules["scissors"])


    # method tests    
    def test_method_can_take_player_choice(self):       
        self.assertEqual("paper", self.game.decide_result(self.player1, self.player2))