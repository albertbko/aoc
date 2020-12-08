import os

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\7input.txt', 'r')

input = inputfile.read().splitlines()

# Part 1
def find_shiny_gold(key):
    colours = bags[key]
    for colour in colours:
        if (colour[1] == 'shiny gold'):
            return True
        else:
            if (find_shiny_gold(colour[1])):
                return True
    return False

bags = {}
# Parse input
for line in input:
    line = line.split()
    key = line[0] + ' ' + line[1]
    
    value = []
    for i in range(2,len(line)):
        if (line[i].isdigit()):
            value.append(tuple((line[i], line[i+1] + ' ' + line[i+2])))
    
    bags[key] = value

num_shiny_colours = 0
# Use recursion to count shiny gold
for colour in bags:
    num_shiny_colours += find_shiny_gold(colour)

print(num_shiny_colours)

#def find_bags_in_shiny(key):
#    num_bags = 0
#    colours = bags[key]
#    for colour in colours:
#        num_bags += int(colour[0]) * find_bags_in_shiny(colour[1])
#        print(colour[1], "equals1", num_bags)
#    print('returning', num_bags + 1)
#    if (num_bags == 0):
#        return 1
#    return num_bags
#
## Part 2
#num_bags_in_gold = 0
#bags_with_shiny_gold = bags['shiny gold']
#for colour in bags_with_shiny_gold:
#    num_bags_in_gold += int(colour[0]) * find_bags_in_shiny(colour[1])
#    print(colour[1], "equals2", num_bags_in_gold)
#
#print(num_bags_in_gold)

list_of_bags = []
num = 0
def find_bags_in_shiny(key):
    colours = bags[key]
    for colour in colours:
        for i in range(int(colour[0])):
            find_bags_in_shiny(colour[1])
            #print(colour[1])
            list_of_bags.append(colour[1])



# Part 2
num_bags_in_gold = 0
bags_with_shiny_gold = bags['shiny gold']
find_bags_in_shiny('shiny gold')

num_bags_in_gold = len(list_of_bags)
print(num_bags_in_gold)