import os

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\6input.txt', 'r')

# groups are separated by \n\n
groups = inputfile.read().split('\n\n')

# Part 1
sum = 0
for i, group in enumerate(groups):
    # strip newline
    group = group.replace('\n', '')
    remove_dupes = "".join(dict.fromkeys(group))
    sum += len(remove_dupes)
print(sum)

# Part 2
sum = 0
for i, group in enumerate(groups):
    all_answered = 0
    # count newlines
    count = group.count('\n') + 1
    # remove newline
    group = group.replace('\n', '')

    for c in group:
        if (group.count(c) == count):
            all_answered += 1
            group = group.replace(c, '')
    sum += all_answered
print(sum)