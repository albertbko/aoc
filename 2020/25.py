import os
import time

def transform(subject_num, loop_size):
    value = 1
    for _ in range(loop_size):
        value = value * subject_num
        value = value % 20201227
    return value

def reverse(public_key, subject_num = 7):
    value = 1
    i = 0
    while(True):
        value = value * subject_num % 20201227
        i += 1
        if value == public_key:
            return i

def part1(input):
    card_public_key = int(input[0])
    door_public_key = int(input[1])

    #card_loop_size = reverse(card_public_key)
    door_loop_size = reverse(door_public_key)

    encryption_key = transform(card_public_key, door_loop_size)
    #encryption_key = transform(door_public_key, card_loop_size)

    return encryption_key

def main():
    input = open(os.path.abspath(os.path.dirname(__file__)) + '\\25input.txt').read().splitlines()
    
    start = time.time()
    print(f'Part1: {part1(input)}')
    print(f'==== Runtime %s ====' % (time.time() - start))

if __name__ == '__main__':
    main()