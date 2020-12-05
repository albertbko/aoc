import os

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\5input.txt', 'r')

input = inputfile.read().splitlines()

seats = []

# Part 1
def get_seat(line, max):
    window = max
    for x in line:
        window /= 2
        if (x == 'F' or x == 'L'):
            max -= window
        #elif (x == 'B' or x == 'R'):
        #    max = max
    
    return max-window

highest_seatID = 0
for line in input:
    seatID = get_seat(line[:7], 128) * 8 + get_seat(line[7:], 8)
    seats.append(seatID)
    if (seatID > highest_seatID):
        highest_seatID = seatID

#print(highest_seatID)

# Part 2
seats.sort()
#print(seats)

previous_seat = 0
for seat in seats:
    if(seat - previous_seat == 2):
        print("found my seat:", seat-1)
    previous_seat = seat