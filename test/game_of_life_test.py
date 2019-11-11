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

  def test_generate_signals_2_3(self):
    result = [(1, 2), (1, 3), (1, 4),
      (2, 2), (2, 4),
      (3, 2), (3, 3), (3, 4)]
      
    self.assertEqual(result, game_of_life.generate_signals((2, 3)))

  def test_generate_signals_1_4(self):
    result = [(0, 3), (0, 4), (0, 5),
      (1, 3), (1, 5),
      (2, 3), (2, 4), (2, 5)]

    self.assertEqual(result, game_of_life.generate_signals((1, 4)))

  def test_generate_signals_0_0(self):
    result = [(-1, -1), (-1, 0), (-1, 1),
      (0, -1), (0, 1),
      (1, -1), (1, 0), (1, 1)]
    self.assertEqual(result, game_of_life.generate_signals((0, 0)))

  def test_generate_signals_for_live_cells_0(self):
    live_cells = [(1, 2), (2, 3)]
    result = [(0, 1), (0, 2), (0, 3), (1, 1), (1, 3), 
	  (2, 1), (2, 2), (2, 3), (1, 2), (1, 3), (1, 4), 
	  (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)]
    self.assertEqual(result, 
	  game_of_life.generate_signals_for_all_live_cells(live_cells))
	  
  def test_generate_signals_for_live_cells_1(self):
    live_cells = [(1, 4), (2, 3), (0, 0)]
    result = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 5), (2, 3), 
	  (2, 4), (2, 5), (1, 2), (1, 3), (1, 4), (2, 2), 
	  (2, 4), (3, 2), (3, 3), (3, 4), (-1, -1), (-1, 0), 
	  (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    self.assertEqual(result, 
	  game_of_life.generate_signals_for_all_live_cells(live_cells))

  def test_count_signals_0(self):
    signals = []
    result = {}
    self.assertEqual(result, game_of_life.count_signals(signals))

  def test_count_signals_1(self):
    signals = [(1, 2)]
    result = {(1, 2): 1}
    self.assertEqual(result, game_of_life.count_signals(signals))
  
  def test_count_signals_2_same_position(self):
    signals = [(1, 2), (1, 2)]
    result = {(1, 2): 2}
    self.assertEqual(result, game_of_life.count_signals(signals))
  
  def test_count_signals_3_2_same_position(self):
    signals = [(1, 2), (2, 1), (1, 2)]
    result = {(1, 2): 2, (2, 1): 1}
    self.assertEqual(result, game_of_life.count_signals(signals))
