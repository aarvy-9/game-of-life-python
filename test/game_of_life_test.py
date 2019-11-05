import unittest
from src import game_of_life

class GameOfLifeTest(unittest.TestCase):
  def test_game_of_life_live_cell_neighbours_0(self):
    self.assertFalse(game_of_life.is_alive(1, 0))

  def test_game_of_life_live_cell_neighbours_1(self):
    self.assertFalse(game_of_life.is_alive(1, 1))
  
  def test_game_of_life_live_cell_neighbours_2(self):
    self.assertTrue(game_of_life.is_alive(1, 2))

  def test_game_of_life_live_cell_neighbours_3(self):
    self.assertTrue(game_of_life.is_alive(1, 3))

  def test_game_of_life_live_cell_neighbours_4(self):
    self.assertFalse(game_of_life.is_alive(1, 4))

  def test_game_of_life_live_cell_neighbours_5(self):
    self.assertFalse(game_of_life.is_alive(1, 5))

  def test_game_of_life_dead_cell_neighbours_0(self):
    self.assertFalse(game_of_life.is_alive(0, 0))

  def test_game_of_life_dead_cell_neighbours_1(self):
    self.assertFalse(game_of_life.is_alive(0, 1))

  def test_game_of_life_dead_cell_neighbours_2(self):
    self.assertFalse(game_of_life.is_alive(0, 2))

  def test_game_of_life_dead_cell_neighbours_3(self):
    self.assertTrue(game_of_life.is_alive(0, 3))

  def test_game_of_life_dead_cell_neighbours_4(self):
    self.assertFalse(game_of_life.is_alive(0, 4))

  def test_game_of_life_dead_cell_neighbours_5(self):
    self.assertFalse(game_of_life.is_alive(0, 5))
