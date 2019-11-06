def is_alive(current_state, number_of_live_neighbors):
  if current_state == 1:
    if number_of_live_neighbors == 2 or number_of_live_neighbors == 3:
      return current_state, number_of_live_neighbors
  else:
    if number_of_live_neighbors == 3:
      return 1, number_of_live_neighbors
  
  return 0, number_of_live_neighbors

#  return current_state and number_of_live_neighbors == 2 or \
#    number_of_live_neighbors == 3