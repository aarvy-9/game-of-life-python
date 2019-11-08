import unittest
from src import game_of_life

#Feedback: what happened to all the tests we wrote?!
#why did we change the tests for is_alive from taking True, 0 to
#this?

class GameOfLifeTest(unittest.TestCase):
  def test_game_of_life_dead_cell_neighbours_1(self):
    self.assertEqual(True, game_of_life.is_alive([[1, 1, 1], [1, 1, 1], [1, 0, 0]], (0, 0)))

  def test_game_of_life_dead_cell_neighbours_2(self):
    self.assertEqual(False, game_of_life.is_alive([[1, 1, 1], [1, 1, 1], [1, 0, 0]], (1, 0)))

  def test_game_of_life_dead_cell_neighbours_3(self):
    self.assertEqual(True, game_of_life.is_alive([[1, 1, 1], [1, 1, 0], [1, 0, 0]], (2, 1)))

  def test_game_of_life_dead_cell_neighbours_4(self):
    self.assertEqual(False, game_of_life.is_alive([[1, 1, 1], [1, 1, 0], [1, 0, 0]], (2, 2)))