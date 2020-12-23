import os
import time

#def shuffle(labels, moves):
#    current_cup = labels[0]
#    picked_up_cups = [0,0,0]
#    for i in range(moves):
#        if (i % 100 == 0):
#            print(i)
#        #print(current_cup)
#        index = labels.index(current_cup) + 1
#        for j in range(3):
#            if (index < len(labels)):
#                picked_up_cups[j] = labels.pop(index)
#            else:
#                picked_up_cups[j] = labels.pop(0)
#        
#        destination = current_cup - 1
#        destination_found = False
#        while not (destination_found):            
#            if (destination < min(labels)):
#                destination = max(labels)
#            try:
#                destination_idx = labels.index(destination) + 1
#                labels[destination_idx:destination_idx] = [picked_up_cups[0], picked_up_cups[1], picked_up_cups[2]]
#                if (labels.index(current_cup) + 1 < len(labels)):
#                    current_cup = labels[labels.index(current_cup) + 1]
#                else:
#                    current_cup = labels[0]
#                destination_found = True
#            except:
#                destination = destination - 1
#        #print(labels)
#        
#
#    return labels

def shuffle(labels, moves):
    current_cup = labels[0]
    picked_up_cups = [0,0,0]
    start = time.time()
    for i in range(moves):
        if (i == 1000):
            print(time.time() - start)
        #print(current_cup)
        index = labels.index(current_cup) + 1
        #for j in range(3):
            #if (index < len(labels)):
                #picked_up_cups[j] = labels.pop(index)
            #else:
                #picked_up_cups[j] = labels.pop(0)
        
        destination = current_cup - 1
        destination_found = False
        while not (destination_found):
            if (destination < min(labels)):
                destination = max(labels)
            try:
                destination_idx = labels.index(destination) + 1
                #labels[:] = [picked_up_cups[0], picked_up_cups[1], picked_up_cups[2]]
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

class Cup():
    def __init__(self, id):
        self.id = id
        self.next = None

def part2(input):
    # part2 has huge n so the solution needs to be a linked-list and use a dict for lookup.
    # solution from https://github.com/tymscar/Advent-Of-Code/blob/master/2020/day23/part2.py
    labels = list(int(x) for x in input)
    highest = max(labels)
    for i in range(highest + 1, 1000001):
        labels.append(i)

    cups = {}
    for label in labels:
        cups[label] = Cup(label)

    for i in range(len(labels) - 1):
        cups[labels[i]].next = cups[labels[i + 1]]
    cups[labels[len(labels) - 1]].next = cups[10]
    for i in range(10, 1000000):
        cups[i].next = cups[i + 1]
    cups[1000000].next = cups[labels[0]]

    current_cup = cups[labels[0]]
    move = 0
    while move < 10000000:
        removed_ids = [current_cup.next.id, current_cup.next.next.id, current_cup.next.next.next.id]
        current_cup.next = current_cup.next.next.next.next
        destination_cup_id = current_cup.id - 1
        if destination_cup_id == 0:
            destination_cup_id = 1000000
        while destination_cup_id in removed_ids:
            destination_cup_id -= 1
            if destination_cup_id == 0:
                destination_cup_id = 1000000

        destination_cup = cups[destination_cup_id]
        cups[removed_ids[2]].next = destination_cup.next
        destination_cup.next = cups[removed_ids[0]]
        current_cup = current_cup.next
        move += 1

    star_1 = cups[1].next.id
    star_2 = cups[1].next.next.id

    return star_1 * star_2


def main():
    input = open(os.path.abspath(os.path.dirname(__file__)) + '\\23input.txt').read()
    
    print(f'Part1: {part1(input)}')
    print(f'Part2: {part2(input)}')

if __name__ == '__main__':
    main()