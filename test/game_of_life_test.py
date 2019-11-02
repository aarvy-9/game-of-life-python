import unittest
from src import game_of_life

class GameOfLifeTest(unittest.TestCase):

  def test_game_of_life(self):
    self.assertTrue(game_of_life.game_of_life())
