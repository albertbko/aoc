import os
import time

def solve_inner_bracket(line, part):
    for i in range(len(line)-1, -1, -1):
        if line[i] == '(':
            start = i
            for j in range(i, len(line)):
                if line[j] == ')':
                    stop = j
                    break
            break
    if (part == 1):
        return_string = ''.join(line[:i]) + str(calculate(line[i+1:j])) + ''.join(line[j+1:])
    else:
        return_string = ''.join(line[:i]) + str(calculate2(line[i+1:j])) + ''.join(line[j+1:])

    return return_string

def calculate(equation):
    # there should be no () in this function
    result = 0
    equation = "".join(equation)
    operands = equation.split(' ')

    result = int(operands[0])
    i = 1
    calculating = True
    while (calculating and len(operands) > 1):
        if (operands[i] == '+'):
            result = result + int(operands[i+1])
            i += 2
        elif (operands[i] == '*'):
            result = result * int(operands[i+1])
            i += 2
        if (i >= len(operands)):
            calculating = False

    return result

def calculate2(equation):
    # there should be no () in this function
    result = 0
    equation = "".join(equation)
    operands = equation.split(' ')

    # '+' takes precedence over '*'
    i = 1
    calculating = True
    new_equation = []
    new_equation.append(operands[0])
    canPop = True
    while (calculating):
        if (operands[i] == '+'):
            if (canPop):
                new_equation.pop()
            sum = int(operands[i-1]) + int(operands[i+1])
            new_equation.append(str(sum))
            operands[i+1] = str(sum)
            i += 2
        elif (operands[i] == '*'):
            new_equation.append(' * ')
            new_equation.append(operands[i+1])
            canPop = True
            i += 2
        if (i >= len(operands)):
            calculating = False

    result = calculate(''.join(new_equation))

    return result

def part1(input):
    sum = 0
    for line in input:
        while ('(' in line):
            line = solve_inner_bracket(list(line), 1)
        answer = calculate(line)
        sum += answer
    return sum

def part2(input):
    sum = 0
    for line in input:
        while ('(' in line):
            line = solve_inner_bracket(list(line), 2)
        answer = calculate2(line)
        sum += answer
    return sum

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    inputfile = open(path + '\\18input.txt', 'r')
    input = inputfile.read().splitlines()

    start = time.time()
    print(f'Part1:{part1(input)}')
    print('==== Runtime %s seconds ====' % (time.time() - start))

    start = time.time()
    print(f'Part2:{part2(input)}')
    print('==== Runtime %s seconds ====' % (time.time() - start))



if __name__ == '__main__':
    main()