import os
import numpy as np

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\11input.txt', 'r')

input = inputfile.read().splitlines()

# Part 1
seating = input.copy()
adjacent_seats = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
rows = len(input)
cols = len(input[0])

def new_seating(rows, cols):
    new_seating = [['' for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if (seating[i][j] == '.'):
                new_seating[i][j] = '.'
            else:
                new_seating[i][j] = decide_seating(i, j)
    return new_seating

def decide_seating(row, col):
    occupied = 0

    for seat in adjacent_seats:
        if ((seat[0] + row) < 0 or (seat[0] + row) > rows - 1):
            continue
        if ((seat[1] + col) < 0 or (seat[1] + col) > cols - 1):
            continue
        if (seating[row + seat[0]][col + seat[1]] == '#'):
            occupied += 1
    
    if (occupied >= 4):
        return 'L'
    elif (occupied == 0):
        return '#'
    else:
        return seating[row][col]

old_seating = seating.copy()
seating = new_seating(rows, cols)
while not (old_seating == seating):
    old_seating = seating.copy()
    seating = new_seating(rows, cols)

occupied_seats = 0
for row in seating:
    occupied_seats += row.count('#')

print(f'Occupied seats: {occupied_seats}')


# Part 2
seating = input.copy()
adjacent_seats = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
rows = len(input)
cols = len(input[0])

def new_seating_part2(rows, cols):
    new_seating = [['' for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if (seating[i][j] == '.'):
                new_seating[i][j] = '.'
            else:
                new_seating[i][j] = decide_seating_part2(i, j)
    return new_seating

def decide_seating_part2(row, col):
    occupied = 0

    for seat in adjacent_seats:
        if ((seat[0] + row) < 0 or (seat[0] + row) > rows - 1):
            continue
        if ((seat[1] + col) < 0 or (seat[1] + col) > cols - 1):
            continue

        multiplier = 1
        while (((seat[0] * multiplier + row) >= 0 and (seat[0] * multiplier + row) <= rows - 1) and ((seat[1] * multiplier + col) >= 0 and (seat[1] * multiplier + col) <= cols - 1)):
            if (seating[row + seat[0] * multiplier][col + seat[1] * multiplier] == '#'):
                occupied += 1
                break
            elif (seating[row + seat[0] * multiplier][col + seat[1] * multiplier] == 'L'):
                break
            multiplier += 1
    
    if (occupied >= 5):
        return 'L'
    elif (occupied == 0):
        return '#'
    else:
        return seating[row][col]

old_seating = seating.copy()
seating = new_seating_part2(rows, cols)
while not (old_seating == seating):
    old_seating = seating.copy()
    seating = new_seating_part2(rows, cols)

occupied_seats = 0
for row in seating:
    occupied_seats += row.count('#')

print(f'Occupied seats: {occupied_seats}')