import os
import time

def part1(input, stopper):
    spoken = {}
    
    for i, number in enumerate(input[:-1]):
        spoken[number] = i + 1      # start at 1
    
    for i in range(len(input), stopper):
        previous = input[i - 1]
        # check if number has been spoken
        if (previous in spoken):
            # if spoken, get age and add to list
            input.append(i - spoken[previous])
            spoken[previous] = i
        else:
            # if not spoken, set age 0 and add to list
            input.append(0)
            spoken[previous] = i
    return input[stopper-1]

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    inputfile = open(path + '\\15input.txt', 'r')

    input = [int(x) for x in inputfile.read().split(',')]
    print(f'Answer:{part1(input, 2020)}')
    print(f'Answer:{part1(input, 30000000)}')


if __name__ == '__main__':
    start = time.time()
    main()
    print("--- Runtime %s seconds ---" % (time.time() - start))