def is_alive(current_state, number_of_live_neighbors):
  if current_state:
    if number_of_live_neighbors == 2 or number_of_live_neighbors == 3:
      return True
  else:
    if number_of_live_neighbors == 3:
      return True
  
  return False