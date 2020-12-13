import os
import math

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\13input.txt', 'r')

input = inputfile.read().splitlines()

depart = int(input[0])
bus_IDs = [int(x) for x in input[1].replace('x,', '').split(',')]

# Part 1
lowest = 100
lowest_bus_ID = 0
for i, bus_ID in enumerate(bus_IDs):
    multiplier = math.ceil(depart / bus_ID)
    if ((bus_ID * multiplier) % depart <= lowest):
        lowest = (bus_ID * multiplier) % depart
        lowest_bus_ID = bus_ID

print(f'Answer:{lowest * lowest_bus_ID}')


# Part 2
bus_IDs = input[1].split(',')

## brute force
#ans = int(bus_IDs[0])
#counter = int(bus_IDs[0])
#i = 1
#searching = True
#while (searching):
#    for i, bus_ID in enumerate(bus_IDs):
#        if (bus_ID == 'x'):
#            continue
#        multiplier = math.ceil(ans / int(bus_ID))
#        if ((int(bus_ID) * multiplier) % ans == i and i == len(bus_IDs)-1):
#            print('found for ', bus_ID, ' at ', ans)
#            print('done')
#            searching = False
#        elif ((int(bus_ID) * multiplier) % ans == i):
#            #print('found for ', bus_ID, ' at ', ans)
#            continue
#        else:
#            break
#    ans += counter

# solved using Chinese Remainder Theorem. Not my solution: https://old.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfo6gu0/
departures = [(t, int(d)) for t, d in enumerate(input[1].split(',')) if d != 'x']
times, deps = zip(*departures)

solved = 1
t = departures[0][0] + departures[0][1]
increment = math.prod(deps[:solved])
while True:
    if all([(t + t_plus) % bus_id == 0 for t_plus, bus_id in departures[:solved+1]]):
        solved += 1
        increment = math.prod(deps[:solved])
        if solved == len(deps):            
            print(f'Answer:{t}')
            break
    t += increment
