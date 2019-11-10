from functools import reduce
import operator

def is_alive(current_status, number_of_live_neighbors):
  return (number_of_live_neighbors == 2 and current_status) or \
    number_of_live_neighbors == 3

def generate_signals(live_cell):
  (x, y) = live_cell
  return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
    (x, y - 1), (x , y + 1),
    (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
	
def generate_signals_for_all_live_cells(live_cells):
  return reduce(operator.add, 
    list(map(lambda x: generate_signals(x), live_cells)))
  #Feedback: we can remove the list( and the ending ) and merge the two lines  
