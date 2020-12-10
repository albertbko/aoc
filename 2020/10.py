import os

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\10input.txt', 'r')

input = list(map(int, inputfile.read().splitlines()))

# Part 1
input.append(0)     # to account for charging outlet
input.sort()
input.append(input[-1] + 3)     # to account for device that's always 3 jolts higher than highest rated

one_jolt = 0
two_jolt = 0
three_jolt = 0
for i, jolt in enumerate(input[:-1]):
    difference = input[i+1] - jolt
    if (difference == 1):
        one_jolt += 1
    elif (difference == 2):
        two_jolt += 1
    elif (difference == 3):
        three_jolt += 1

print(one_jolt, two_jolt, three_jolt)
print(one_jolt * three_jolt)

# Part 2
inputfile = open(path + '\\10input.txt', 'r')
input = list(map(int, inputfile.read().splitlines()))
input.sort()
input = input + [max(input) + 3]

ans = {}
ans[0] = 1
# Tribonacci
for a in input:
    ans[a] = ans.get(a - 1, 0) + ans.get(a - 2, 0) + ans.get(a - 3, 0)
print(f'Answer: {ans[input[-1]]}')