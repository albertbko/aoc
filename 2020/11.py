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

def new_seating(rows, cols, part):
    new_seating = [['' for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if (seating[i][j] == '.'):
                new_seating[i][j] = '.'
            else:
                new_seating[i][j] = decide_seating(i, j, part)
    return new_seating

def decide_seating(row, col, part):
    occupied = 0
    if (part == 1):
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
    elif (part == 2):
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

def count_occupied_seats():
    occupied_seats = 0
    for row in seating:
        occupied_seats += row.count('#')
    return occupied_seats

old_seating = seating.copy()
seating = new_seating(rows, cols, 1)
while not (old_seating == seating):
    old_seating = seating.copy()
    seating = new_seating(rows, cols, 1)

print(f'Occupied seats: {count_occupied_seats()}')


# Part 2
seating = input.copy()
rows = len(input)
cols = len(input[0])

old_seating = seating.copy()
seating = new_seating(rows, cols, 2)
while not (old_seating == seating):
    old_seating = seating.copy()
    seating = new_seating(rows, cols, 2)

print(f'Occupied seats: {count_occupied_seats()}')