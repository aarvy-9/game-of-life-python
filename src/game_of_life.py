def is_alive(current_state, number_of_live_neighbors):
  return (number_of_live_neighbors == 2 and current_state) or number_of_live_neighbors == 3

def generate_signals(i, j):
  return [(i-1, j-1), (i, j-1), (i+1, j-1), (i+1, j), (i+1, j+1), (i, j+1), (i-1, j), (i-1, j-1)]