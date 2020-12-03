import os

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\3input.txt', 'r')

input = inputfile.read().splitlines()

# Part 1
trees = 0
length = len(input[0])
col = 0

for i, line in enumerate(input):
    if (i == 0):
        continue
    
    col += 3

    if (line[col % length] == '#'):
        trees += 1

#print(trees)

# Part 2
r1_d1 = 0       #right one down one
r3_d1 = 0       #right three down one
r5_d1 = 0       #right five down one
r7_d1 = 0       #right seven down one
r1_d2 = 0       #right one down two
length = len(input[0])
col1, col2, col3, col4, col5 = 0, 0, 0, 0, 0
size = len(input)

for i in range(size):
    if (i == 0):
        continue

    col1 += 1
    col2 += 3
    col3 += 5
    col4 += 7
    col5 += 1

    if (input[i][col1 % length] == '#'):
        r1_d1 += 1
    
    if (input[i][col2 % length] == '#'):
        r3_d1 += 1
    
    if (input[i][col3 % length] == '#'):
        r5_d1 += 1
    
    if (input[i][col4 % length] == '#'):
        r7_d1 += 1
    
    if (i*2 <= size and input[i * 2][col5 % length] == '#'):
        r1_d2 += 1

print(r1_d1 * r3_d1 * r5_d1 * r7_d1 * r1_d2)