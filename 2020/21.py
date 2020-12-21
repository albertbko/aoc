import os

def solve_matches(allergens):
    solved_allergens = {}
    matched = []
    solving = True
    while (solving):
        if len(solved_allergens) == len(allergens):
            solving = False
            break
        for allergen in allergens:
            # scrub matched values from possible matches
            possible = allergens[allergen]
            for match in matched:
                if match in possible and len(possible) > 1:
                    possible.remove(match)
            allergens[allergen] = possible
            # if only 1 possible match left, found answer
            if len(allergens[allergen]) == 1:
                solved_allergens[allergen] = allergens[allergen]
                matched.append(allergens[allergen][0])

    return solved_allergens

def get_intersections(allergen, items, ingredients_list):
    intersection = items
    for ingredients in ingredients_list:
        if allergen in ingredients[1]:
            intersection = list(set(intersection) & set(ingredients[0]))

    return intersection

def part1(input):
    ingredients_list = []
    allergens = {}
    for line in input:
        ingredients = line[:line.index('(')-1].splitlines()
        ingredients = ingredients[0].split(' ')
        contains = line[line.index('('):].replace('(contains ', '').replace(')', '').split(', ')
        ingredients_list.append(tuple((ingredients, contains)))
        
    for i, items in enumerate(ingredients_list):
        contains = items[1]
        for allergen in contains:
            if allergen not in allergens:
                allergens[allergen] = get_intersections(allergen, items[0], ingredients_list)
    
    allergens = solve_matches(allergens)
    # allergens values are in list of list, so flatten to single list
    allergens = [x for sublist in allergens.values() for x in sublist]

    count = 0
    for items in ingredients_list:
        for item in items[0]:
            if item not in allergens:
                count += 1
                #print(item)
    
    return count

def part2(input):
    ingredients_list = []
    allergens = {}
    for line in input:
        ingredients = line[:line.index('(')-1].splitlines()
        ingredients = ingredients[0].split(' ')
        contains = line[line.index('('):].replace('(contains ', '').replace(')', '').split(', ')
        ingredients_list.append(tuple((ingredients, contains)))
        
    for i, items in enumerate(ingredients_list):
        contains = items[1]
        for allergen in contains:
            if allergen not in allergens:
                allergens[allergen] = get_intersections(allergen, items[0], ingredients_list)
    
    allergens = solve_matches(allergens)
    allergic_ingredients = sorted(list(allergens.keys()))
    dangerous_list = []
    for ingredient in allergic_ingredients:
        dangerous_list.append(allergens[ingredient][0])

    return ','.join(dangerous_list)

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    inputfile = open(path + '\\21input.txt', 'r')
    input = inputfile.read().splitlines()

    print(f'Part1: {part1(input)}')
    print(f'Part2: {part2(input)}')

if __name__ == '__main__':
    main()