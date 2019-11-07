def is_alive(current_state, number_of_live_neighbors):
  return (number_of_live_neighbors == 2 and current_state) or number_of_live_neighbors == 3 #Feedback: code runs off and wraps.

def generate_signals(i, j): #Feedback: let's take in a tuple instead of two parameters
  return [(i-1, j-1), (i, j-1), (i+1, j-1), (i+1, j), (i+1, j+1), (i, j+1), (i-1, j), (i-1, j-1)] #Feedback: space arond operators like -