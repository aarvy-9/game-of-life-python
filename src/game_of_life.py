def generate_signals(index):
  return [(index[0] - 1, index[1] - 1), (index[0] - 1, index[1]), (index[0] - 1, index[1] + 1), (index[0], index[1] - 1),
          (index[0], index[1] + 1), (index[0] + 1, index[1] - 1), (index[0] + 1, index[1]), (index[0] + 1, index[1] + 1)]

def get_live_neighbours_count(universe, index):
  return len(list(filter(lambda x: universe[x[0]][x[1]] == 1, filter(lambda x: -1 not in x and (x[0] < len(universe)) and (x[1] < len(universe[0])), generate_signals(index)))))

def is_alive(universe, index):
  number_of_live_neighbors = get_live_neighbours_count(universe, index)
  return (number_of_live_neighbors == 2 and universe[index[0]][index[1]]) or number_of_live_neighbors == 3
