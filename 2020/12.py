import os

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\12input.txt', 'r')

input = inputfile.read().splitlines()

# Part 1
x, y = 0, 0
location =[x, y]
heading = 'E'

def move(location, direction, distance):
    if (direction == 'N'):
        location[1] += distance
    elif (direction == 'E'):
        location[0] += distance
    elif (direction == 'S'):
        location[1] -= distance
    elif (direction == 'W'):
        location[0] -= distance
    
    return location

def change_heading(heading, direction, angle):
    cardinal_direction = ['E', 'S', 'W', 'N']
    turns = int(angle / 90)
    current_heading_index = cardinal_direction.index(heading)

    if (direction == 'L'):
        heading = cardinal_direction[(current_heading_index - turns) % 4]
    elif (direction == 'R'):
        heading = cardinal_direction[(current_heading_index + turns) % 4]

    return heading

for i, instruction in enumerate(input):
    direction = instruction[0]
    distance = int(instruction[1:])

    if (direction == 'N' or direction == 'S' or direction == 'W' or direction == 'E'):
        location = move(location, direction, distance)
    elif (direction == 'F'):
        location = move(location, heading, distance)
    elif (direction == 'L' or direction == 'R'):
        heading = change_heading(heading, direction, distance)

print(f'Manhattan distance: {abs(location[0] + location[1])}')


# Part 2
x, y = 0, 0
location =[x, y]
waypoint = [x + 10, y + 1]      # the waypoint starts 10 units east and 1 unit north relative to the ship
heading = 'E'

def move_ship(location, waypoint, distance):
    for _ in range(distance):
        location[0] += waypoint[0]
        location[1] += waypoint[1]
    return location

def rotate_waypoint(waypoint, direction, angle):
    turns = int((angle / 90) % 4)
    temp = 0

    if ((turns == 1 and direction == 'L') or (turns == 3 and direction == 'R')):
        # sign for north or south always changes when rotating left: north(+) -> west(-), south(-) -> east(+)
        waypoint[1] *= -1
        # x becomes y and y becomes x
        temp = waypoint[0]
        waypoint[0] = waypoint[1]
        waypoint[1] = temp
    elif (turns == 2):  #direction doesn't matter here
        # for 180 deg turn, only signs change on x and y
        waypoint[0] *= -1
        waypoint[1] *= -1
    elif ((turns == 3 and direction == 'L') or (turns == 1 and direction == 'R')):
        # east(+) becomes south(-), north(+) becomes east(+), west(-) becomes north(+), and south(-) becomes west(-)
        # sign for east or west always changes
        waypoint[0] *= -1
        # x becomes y and y becomes x
        temp = waypoint[0]
        waypoint[0] = waypoint[1]
        waypoint[1] = temp
    #elif (turns == 4):
        # no change
    
    return waypoint

for i, instruction in enumerate(input):
    direction = instruction[0]
    distance = int(instruction[1:])

    if (direction == 'N' or direction == 'S' or direction == 'W' or direction == 'E'):
        waypoint = move(waypoint, direction, distance)
    elif (direction == 'F'):
        location = move_ship(location, waypoint, distance)
    elif (direction == 'L' or direction == 'R'):
        waypoint = rotate_waypoint(waypoint, direction, distance)

print(f'Manhattan distance: {abs(location[0]) + abs(location[1])}')