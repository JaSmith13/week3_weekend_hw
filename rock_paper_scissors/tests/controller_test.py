import unittest
from models.game import *
from controllers.controller import display_winner

class TestController(unittest.TestCase):

    # def setUp(self):
        

    #swap the return statements in controller.py to make this pass
    def test_display_winner(self):
        self.assertEqual("rock", display_winner("rock", "scissors"))