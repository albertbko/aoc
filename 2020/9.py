import os

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\9input.txt', 'r')

input = inputfile.read().splitlines()
puzzle_input = [int(i) for i in input]

part2_start = 0
# Part 1
def find_match(i, line):
    # Grab the 25-number preamble
    preamble = puzzle_input[i:i+preamble_length]
    for j, first_value in enumerate(preamble):
        complement = line - first_value
        for second_value in preamble[j:]:
            if (second_value == complement):
                return True
    return False

preamble_length = 25
for i, line in enumerate(puzzle_input[preamble_length:]):
    if not (find_match(i, line)):
        print("Found the number:", line)
        part2_start = line
        break

# Part 2
searching = True
i = 0
while (searching):
    contiguous_range = []
    for value in puzzle_input[i:]:
        contiguous_range.append(value)
        if (sum(contiguous_range) > part2_start):
            break
        elif (sum(contiguous_range) == part2_start):
            contiguous_range.sort()
            #print("smallest:", contiguous_range[0])
            #print("largest:", contiguous_range[-1])
            print(contiguous_range[0] + contiguous_range[-1])
            searching = False
    i += 1
