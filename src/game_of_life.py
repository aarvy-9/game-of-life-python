def increment_count(count):
  return count + 1

def neighbour_count(initial_state, row, col, cell_type):

  # cell count mutated in this function

  neighbours = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
  cell_count = 0

  for neighbour in neighbours:
    if not (row + neighbour[0] < 0 or col + neighbour[1] < 0 or row + neighbour[0] > len(initial_state) - 1 or col + neighbour[1] > len(initial_state[0]) - 1):
      if initial_state[row + neighbour[0]][col + neighbour[1]] == 1 and cell_type == 1:
        cell_count = increment_count(cell_count)
      elif initial_state[row + neighbour[0]][col + neighbour[1]] == 1 and cell_type == 0:
        cell_count = increment_count(cell_count)
  
  # print(cell_count, row, col, cell_type, initial_state)
  return cell_count


def game_of_life(initial_state):

  # next_generation mutated in this function:
  # For now created only for 1 next generation. can extend it to multiple geneations using a while loop

  next_generation = [[0 for col in range(len(initial_state[0]))] for row in range(len(initial_state))]
  
  for i in range(len(initial_state)):
    for j in range(len(initial_state[0])):
      if initial_state[i][j] == 1 and 2 <= neighbour_count(initial_state, i, j, 1) <= 3:
          next_generation[i][j] = 1
      elif neighbour_count(initial_state, i, j, 0) == 3:
          next_generation[i][j] = 1

  return next_generation

initial_state = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(game_of_life(initial_state))
