import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player1 = Player('Scott', 'scissors')
        self.player2 = Player('Regina', 'rock')

    def test_player_has_name(self):
        self.assertEqual('Scott', self.player1.name)

    def test_player_has_choice(self):
        self.assertEqual('scissors', self.player1.choice)