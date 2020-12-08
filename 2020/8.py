import os

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\8input.txt', 'r')

input = inputfile.read().splitlines()

# Part 1
i = 0
acc = 0
processed_instructions = []
while (i < len(input)):
    try:
        processed_instructions.index(i)
        # if exception hasn't been thrown, the instruction has already been executed.
        break
    except:
        processed_instructions.append(i)
        instruction = input[i].split(' ')
        if (instruction[0] == 'nop'):
            i += 1
        elif (instruction[0] == 'acc'):
            if (instruction[1][0] == '-'):
                acc -= int(instruction[1].replace('-', ''))
            elif (instruction[1][0] == '+'):
                acc += int(instruction[1].replace('+', ''))
            i += 1
        elif (instruction[0] == 'jmp'):
            if (instruction[1][0] == '-'):
                i -= int(instruction[1].replace('-', ''))
            elif (instruction[1][0] == '+'):
                i += int(instruction[1].replace('+', ''))

print(acc)

# Part 2
new_instructions = []
for i in range(len(input)):
    instruction = input[i].split(' ')
    if (instruction[0] == 'jmp'):
        new_instructions.append(tuple((i, 'nop ' + instruction[1])))

for new_instruction in new_instructions:
    old_instruction = input[new_instruction[0]]
    input[new_instruction[0]] = new_instruction[1]

    i = 0
    acc = 0
    processed_instructions = []
    while (i < len(input)):
        try:
            processed_instructions.index(i)
            # if exception hasn't been thrown, the instruction has already been executed.
            break
        except:
            processed_instructions.append(i)
            instruction = input[i].split(' ')
            if (instruction[0] == 'nop'):
                i += 1
            elif (instruction[0] == 'acc'):
                if (instruction[1][0] == '-'):
                    acc -= int(instruction[1].replace('-', ''))
                elif (instruction[1][0] == '+'):
                    acc += int(instruction[1].replace('+', ''))
                i += 1
            elif (instruction[0] == 'jmp'):
                if (instruction[1][0] == '-'):
                    i -= int(instruction[1].replace('-', ''))
                elif (instruction[1][0] == '+'):
                    i += int(instruction[1].replace('+', ''))
    if (i >= len(input)):
        print(acc)
    
    # Change back to original (old instruction) after attempt
    input[new_instruction[0]] = old_instruction