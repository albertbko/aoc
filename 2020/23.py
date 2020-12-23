import os

def shuffle(labels, moves):
    current_cup = labels[0]
    picked_up_cups = [0,0,0]
    for i in range(moves):
        if (i % 100 == 0):
            print(i)
        #print(current_cup)
        index = labels.index(current_cup) + 1
        for j in range(3):
            if (index < len(labels)):
                picked_up_cups[j] = labels.pop(index)
            else:
                picked_up_cups[j] = labels.pop(0)
        
        destination = current_cup - 1
        destination_found = False
        while not (destination_found):            
            if (destination < min(labels)):
                destination = max(labels)
            try:
                destination_idx = labels.index(destination) + 1
                labels[destination_idx:destination_idx] = [picked_up_cups[0], picked_up_cups[1], picked_up_cups[2]]
                if (labels.index(current_cup) + 1 < len(labels)):
                    current_cup = labels[labels.index(current_cup) + 1]
                else:
                    current_cup = labels[0]
                destination_found = True
            except:
                destination = destination - 1
        #print(labels)
        

    return labels


def part1(input):
    labels = list(int(x) for x in input)
    result = shuffle(labels, 100)
    
    ans = []
    start = result.index(1) + 1
    for i in range(len(result) - 1):
        ans.append(result[(start + i) % len(result)])
    
    
    return ''.join(str(x) for x in ans)

def part2(input):
    labels = list(int(x) for x in input)
    highest = max(labels)
    for i in range(highest + 1, 1000001):
        labels.append(i)

    result = shuffle(labels, 10000000)
    
    ans = []
    cup1 = result.index(1)
    if cup1 + 2 > len(result):
        cup2 = result[(cup1 + 1) % len(result) - 1]
        cup3 = result[(cup1 + 2) % len(result) - 1]
    else:
        cup2 = result[cup1 + 1]
        cup3 = result[cup1 + 2]

    return cup2 * cup3

def main():
    input = open(os.path.abspath(os.path.dirname(__file__)) + '\\23input_test.txt').read()
    
    print(f'Part1: {part1(input)}')
    print(f'Part2: {part2(input)}')

if __name__ == '__main__':
    main()