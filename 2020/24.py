import os
import time

# coordinates in hex grid: https://www.redblobgames.com/grids/hexagons/
# used the doubled coordinates (double-width)
def get_coordinates(directions):
    x = 0
    y = 0

    for direction in directions:
        if direction == 'e':
            x += 2
        elif direction == 'se':
            x += 1
            y += 1
        elif direction == 'sw':
            x -= 1
            y += 1
        elif direction == 'w':
            x -= 2
        elif direction == 'nw':
            x -= 1
            y -= 1
        elif direction == 'ne':
            x += 1
            y -= 1
            
    return (x,y)

def part1(input):
    coordinates = {}
    for line in input:
        flip = list(line)
        delimited = []
        index = 0
        while (index < len(flip)):
            direction = ''.join(flip[index:index + 2])
            if direction == 'se' or direction == 'sw' or direction == 'nw' or direction == 'ne':
                delimited.append(direction)
                index += 2
            elif flip[index] == 'e' or flip[index] == 'w':
                delimited.append(flip[index])
                index += 1
        xy = get_coordinates(delimited)
        coordinates[xy] = (coordinates.get(xy, 0) + 1) % 2
    
    return sum(value == 1 for value in coordinates.values())

def part2(input):
    # day 1
    coordinates = {}
    for line in input:
        flip = list(line)
        delimited = []
        index = 0
        while (index < len(flip)):
            direction = ''.join(flip[index:index + 2])
            if direction == 'se' or direction == 'sw' or direction == 'nw' or direction == 'ne':
                delimited.append(direction)
                index += 2
            elif flip[index] == 'e' or flip[index] == 'w':
                delimited.append(flip[index])
                index += 1
        xy = get_coordinates(delimited)
        coordinates[xy] = (coordinates.get(xy, 0) + 1) % 2
        
    # days 2-100
    for i in range(1, 101):
        # add neighbours
        for tile in list(coordinates):
            coordinates[tuple((tile[0] + 2, tile[1]))] = coordinates.get(tuple((tile[0] + 2, tile[1])), 0)
            coordinates[tuple((tile[0] + 1, tile[1] + 1))] = coordinates.get(tuple((tile[0] + 1, tile[1] + 1)), 0)
            coordinates[tuple((tile[0] - 1, tile[1] + 1))] = coordinates.get(tuple((tile[0] - 1, tile[1] + 1)), 0)
            coordinates[tuple((tile[0] - 2, tile[1]))] = coordinates.get(tuple((tile[0] - 2, tile[1])), 0)
            coordinates[tuple((tile[0] - 1, tile[1] - 1))] = coordinates.get(tuple((tile[0] - 1, tile[1] - 1)), 0)
            coordinates[tuple((tile[0] + 1, tile[1] - 1))] = coordinates.get(tuple((tile[0] + 1, tile[1] - 1)), 0)

        new_setup = {}
        for tile in coordinates:
            #check adjacent tiles:
            black = 0
            if (coordinates.get(tuple((tile[0] + 2, tile[1])), 0) == 1):
                black += 1
            if (coordinates.get(tuple((tile[0] + 1, tile[1] + 1)), 0) == 1):
                black += 1
            if (coordinates.get(tuple((tile[0] - 1, tile[1] + 1)), 0) == 1):
                black += 1
            if (coordinates.get(tuple((tile[0] - 2, tile[1])), 0) == 1):
                black += 1
            if (coordinates.get(tuple((tile[0] - 1, tile[1] - 1)), 0) == 1):
                black += 1
            if (coordinates.get(tuple((tile[0] + 1, tile[1] - 1)), 0) == 1):
                black += 1

            if (coordinates.get(tile) == 1 and (black == 0 or black > 2)):
                new_setup[tile] = 0
            elif (coordinates.get(tile) == 0 and black == 2):
                new_setup[tile] = 1
            else:
                new_setup[tile] = coordinates.get(tile, 0)
        coordinates = new_setup
        #print('Day', i ,sum(value == 1 for value in coordinates.values()))

    return sum(value == 1 for value in coordinates.values())

def main():
    input = open(os.path.abspath(os.path.dirname(__file__)) + '\\24input.txt').read().splitlines()
    
    start = time.time()
    print(f'Part1: {part1(input)}')
    print(f'==== Runtime %s ====' % (time.time() - start))

    start = time.time()
    print(f'Part2: {part2(input)}')
    print(f'==== Runtime %s ====' % (time.time() - start))

if __name__ == '__main__':
    main()