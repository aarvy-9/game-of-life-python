import unittest
from src import game_of_life

class GameOfLifeTest(unittest.TestCase):
  def test_game_of_life_live_cell_neighbours_0(self):
    self.assertEqual([False, 0], game_of_life.is_alive(True, 0))

  def test_game_of_life_live_cell_neighbours_1(self):
    self.assertEqual([False, 1], game_of_life.is_alive(True, 1))
  
  def test_game_of_life_live_cell_neighbours_2(self):
    self.assertEqual([True, 2], game_of_life.is_alive(True, 2)) 

  def test_game_of_life_live_cell_neighbours_3(self):
    self.assertEqual([True, 3], game_of_life.is_alive(True, 3)) 

  def test_game_of_life_live_cell_neighbours_4(self):
    self.assertEqual([False, 4], game_of_life.is_alive(True, 4))

  def test_game_of_life_live_cell_neighbours_5(self):
    self.assertEqual([False, 5], game_of_life.is_alive(True, 5))

  def test_game_of_life_dead_cell_neighbours_0(self):
    self.assertEqual([False, 0], game_of_life.is_alive(False, 0))

  def test_game_of_life_dead_cell_neighbours_1(self):
    self.assertEqual([False, 1], game_of_life.is_alive(False, 1))

  def test_game_of_life_dead_cell_neighbours_2(self):
    self.assertEqual([False, 2], game_of_life.is_alive(False, 2))

  def test_game_of_life_dead_cell_neighbours_3(self):
    self.assertEqual([True, 3], game_of_life.is_alive(False, 3))

  def test_game_of_life_dead_cell_neighbours_4(self):
    self.assertEqual([False, 4], game_of_life.is_alive(False, 4))

  def test_game_of_life_dead_cell_neighbours_5(self):
    self.assertEqual([False, 5], game_of_life.is_alive(False, 5))
