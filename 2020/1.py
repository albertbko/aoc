import os

path = os.path.abspath(os.path.dirname(__file__))

inputfile = open(path +  '\\1input.txt', 'r')
#print(path +  '\\1input.txt')

input = inputfile.read().splitlines()
#print(input)

# Part 1
goal = 2020
for i, number in enumerate(input):
    complimentarySum = goal - int(number)
    if (str(complimentarySum) in input[i:]):
        #print("FOUND:", number, complimentarySum)
        answer = int(number) * complimentarySum
        print(answer)
        break

# Part 2
for i, number in enumerate(input):
    complimentary = goal - int(number)
    for j, number2 in enumerate(input[i:]):
        complimentary2 = complimentary - int(number2)
        if (str(complimentary2) in input[j:]):
            #print("FOUND:", number, complimentary2, number2)
            answer = int(number) * complimentary2 * int(number2)
            print(answer)
            break