def generate_signals(i):
    return [(i[0] - 1, i[1] - 1), (i[0] - 1, i[1]), (i[0] - 1, i[1] + 1), 
            (i[0], i[1] - 1), (i[0], i[1] + 1), 
            (i[0] + 1, i[1] - 1), (i[0] + 1, i[1]), (i[0] + 1, i[1] + 1)]


def get_live_neighbours_count(universe, index):
    valid_signals = filter(lambda x: 
                           -1 not in x and (x[0] < len(universe)) and 
                           (x[1] < len(universe[0])), 
                           generate_signals(index))
    return len(list(filter(lambda x: universe[x[0]][x[1]] == 1, 
                           valid_signals)))


def is_alive(current_status, number_of_live_neighbors):
    return (number_of_live_neighbors == 2 and current_status) or \
           number_of_live_neighbors == 3
