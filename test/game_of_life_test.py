import unittest
from src import game_of_life

class GameOfLifeTest(unittest.TestCase):

  def test_game_of_life(self):
    initial_state = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]
    self.assertTrue([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]], game_of_life.game_of_life(initial_state))
