import unittest
from src import game_of_life

class GameOfLifeTest(unittest.TestCase):
  def test_game_of_life_live_cell_neighbours_0(self):
    self.assertEqual(False, game_of_life.is_alive(True, 0))

  def test_game_of_life_live_cell_neighbours_1(self):
    self.assertEqual(False, game_of_life.is_alive(True, 1))
  
  def test_game_of_life_live_cell_neighbours_2(self):
    self.assertEqual(True, game_of_life.is_alive(True, 2)) 

  def test_game_of_life_live_cell_neighbours_3(self):
    self.assertEqual(True, game_of_life.is_alive(True, 3)) 

  def test_game_of_life_live_cell_neighbours_4(self):
    self.assertEqual(False, game_of_life.is_alive(True, 4))

  def test_game_of_life_live_cell_neighbours_5(self):
    self.assertEqual(False, game_of_life.is_alive(True, 5))

  def test_game_of_life_dead_cell_neighbours_0(self):
    self.assertEqual(False, game_of_life.is_alive(False, 0))

  def test_game_of_life_dead_cell_neighbours_1(self):
    self.assertEqual(False, game_of_life.is_alive(False, 1))

  def test_game_of_life_dead_cell_neighbours_2(self):
    self.assertEqual(False, game_of_life.is_alive(False, 2))

  def test_game_of_life_dead_cell_neighbours_3(self):
    self.assertEqual(True, game_of_life.is_alive(False, 3))

  def test_game_of_life_dead_cell_neighbours_4(self):
    self.assertEqual(False, game_of_life.is_alive(False, 4))

  def test_game_of_life_dead_cell_neighbours_5(self):
    self.assertEqual(False, game_of_life.is_alive(False, 5))

#Feedback: code runs off and wraps	
  def test_generate_signals_2_3(self):
    self.assertEqual([(1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 3), (1, 2)], game_of_life.generate_signals((2, 3)))
	
  def test_generate_signals_1_4(self):
    self.assertEqual([(0, 3), (1, 3), (2, 3), (2, 4), (2, 5), (1, 5), (0, 4), (0, 3)], game_of_life.generate_signals((1, 4)))
	
  def test_generate_signals_0_0(self):
    self.assertEqual([(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1)], game_of_life.generate_signals((0, 0)))
