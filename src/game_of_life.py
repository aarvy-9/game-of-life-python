from functools import reduce
from collections import Counter
import operator
from time import sleep
import os

def is_alive(current_status, number_of_live_neighbors):
  return (number_of_live_neighbors == 2 and current_status) or \
    number_of_live_neighbors == 3

def generate_signals(live_cell):
  (x, y) = live_cell
  return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
    (x, y - 1), (x , y + 1),
    (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
	
def generate_signals_for_all_live_cells(live_cells):
  return reduce(operator.add, map(generate_signals, live_cells))

def count_signals(signals):
  return dict(Counter(signals))

def next_generation(live_cells):
  all_live_signals = generate_signals_for_all_live_cells(live_cells)
  signal_count = count_signals(all_live_signals)
  return list(filter(lambda x: is_alive(x in live_cells, signal_count[x]), 
                signal_count)) # Feedback: what does x mean?

def display(live_cells):
  print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
  x = [i[0] for i in live_cells]
  y = [i[1] for i in live_cells]
  min_, max_ = min(min(x), min(y)), max(max(x), max(y))
  for i in range(min_ - 1, max_ + 1):
    print(''.join('X' if (i, j) in live_cells else ' ' 
      for j in range(min_ - 1, max_ + 1)))

def game_of_life():
  live_cells = [(0, 0), (0, 1), (0, 2)]
  while True:
    os.system('cls')
    display(live_cells)
    live_cells = next_generation(live_cells) # Feedback: avoid mutation, honor immutability
    sleep(1)

if __name__ == '__main__':
  game_of_life()
