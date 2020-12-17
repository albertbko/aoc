import os
import itertools
import time

def state_for_new_space(coordinate, state):
    adjacent_cubes = [list(i) for i in itertools.product([-1, 0, 1], repeat=3)]

    active_count = 0
    for neighbour in adjacent_cubes:
        if neighbour == [0,0,0]:
            continue
        new_coordinate = coordinate[0] + neighbour[0], coordinate[1] + neighbour[1], coordinate[2] + neighbour[2]
        try:
            if state[new_coordinate] == '#':
                active_count += 1
        except:
            pass

    if active_count == 3:
        return '#'
    else:
        return '.'

def cycle(state):
    adjacent_cubes = [list(i) for i in itertools.product([-1, 0, 1], repeat=3)]
    new_state = {}

    for coordinate in state:
        active_count = 0
        for neighbour in adjacent_cubes:
            if neighbour == [0,0,0]:
                continue
            new_coordinate = coordinate[0] + neighbour[0], coordinate[1] + neighbour[1], coordinate[2] + neighbour[2]
            try:
                if state[new_coordinate] == '#':
                    active_count += 1
            except:
                new_state[new_coordinate] = state_for_new_space(new_coordinate, state)
        
        if state[coordinate] == '#' and (active_count == 2 or active_count == 3):
            new_state[coordinate] = '#'
        elif state[coordinate] == '.' and active_count == 3:
            new_state[coordinate] = '#'
        else:
            new_state[coordinate] = '.'
    
    return new_state

def state_for_new_space2(coordinate, state):
    adjacent_cubes = [list(i) for i in itertools.product([-1, 0, 1], repeat=4)]

    active_count = 0
    for neighbour in adjacent_cubes:
        if neighbour == [0,0,0,0]:
            continue
        new_coordinate = coordinate[0] + neighbour[0], coordinate[1] + neighbour[1], coordinate[2] + neighbour[2], coordinate[3] + neighbour[3]
        try:
            if state[new_coordinate] == '#':
                active_count += 1
        except:
            pass

    if active_count == 3:
        return '#'
    else:
        return '.'

def cycle2(state):
    adjacent_cubes = [list(i) for i in itertools.product([-1, 0, 1], repeat=4)]
    new_state = {}

    for coordinate in state:
        active_count = 0
        for neighbour in adjacent_cubes:
            if neighbour == [0,0,0,0]:
                continue
            new_coordinate = coordinate[0] + neighbour[0], coordinate[1] + neighbour[1], coordinate[2] + neighbour[2], coordinate[3] + neighbour[3]
            try:
                if state[new_coordinate] == '#':
                    active_count += 1
            except:
                new_state[new_coordinate] = state_for_new_space2(new_coordinate, state)
        
        if state[coordinate] == '#' and (active_count == 2 or active_count == 3):
            new_state[coordinate] = '#'
        elif state[coordinate] == '.' and active_count == 3:
            new_state[coordinate] = '#'
        else:
            new_state[coordinate] = '.'
    
    return new_state

def part1(initial_state):
    state = initial_state
    for i in range(6):
        state = cycle(state)

    return sum(value == '#' for value in state.values())

def part2(initial_state):
    state = initial_state
    for i in range(6):
        state = cycle2(state)

    return sum(value == '#' for value in state.values())

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    inputfile = open(path + '\\17input.txt', 'r')

    input = inputfile.read().splitlines()

    initial_state = {}
    for row in range(len(input)):
        for col in range(len(input[0])):
            initial_state[col,row,0] = input[row][col]

    initial_state2 = {}
    for row in range(len(input)):
        for col in range(len(input[0])):
            initial_state2[col,row,0,0] = input[row][col]

    start = time.time()
    print(f'Answer:{part1(initial_state)}')
    print('=== Runtime %s seconds ===' % (time.time() - start))
    
    start = time.time()
    print(f'Answer:{part2(initial_state2)}')
    print('=== Runtime %s seconds ===' % (time.time() - start))


if __name__ == '__main__':
    main()