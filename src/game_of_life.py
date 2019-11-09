#Feedback: code is wrapping on multiple lines making it hard to read.
def generate_signals(index):
  return [(index[0] - 1, index[1] - 1), (index[0] - 1, index[1]), (index[0] - 1, index[1] + 1), (index[0], index[1] - 1), (index[0], index[1] + 1), (index[0] + 1, index[1] - 1), (index[0] + 1, index[1]), (index[0] + 1, index[1] + 1)]

def get_live_neighbours_count(universe, index):
  return len(list(filter(lambda x: universe[x[0]][x[1]] == 1, filter(lambda x: -1 not in x and (x[0] < len(universe)) and (x[1] < len(universe[0])), generate_signals(index)))))

def is_alive(current_status, number_of_live_neighbors):
  return (number_of_live_neighbors == 2 and current_status) or number_of_live_neighbors == 3

def main_function(universe):
  for i in range(len(universe)):
    for j in range(len(universe[0])):
      is_alive(universe[i][j], get_live_neighbours_count(universe, (i, j)))


main_function([[True, True, True], [True, True, True], [True, False, False]])