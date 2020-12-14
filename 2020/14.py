import os

def get_address_and_value(line):
    line = line.replace('mem[', '')
    line = line.replace(']', '')
    
    return line.split(' = ')[0], line.split(' = ')[1]

def apply_bitmask(mask, value):
    binary_value = '{0:036b}'.format(int(value))
    new_value = list('000000000000000000000000000000000000')

    for i in range(len(binary_value)-1, -1, -1):        # start at len-1 which is 36-1. Stop at -1, increment by -1
        if (mask[i] == '1'):
            new_value[i] = '1'
        elif (mask[i] == '0'):
            new_value[i] = '0'
        elif (mask[i] == 'X'):
            new_value[i] = binary_value[i]

    return int("".join(new_value), 2)

def apply_bitmask2(mask, value):
    binary_value = '{0:036b}'.format(int(value))
    new_value = list('000000000000000000000000000000000000')

    for i in range(len(binary_value)-1, -1, -1):        # start at len-1 which is 36-1. Stop at -1, increment by -1
        if (mask[i] == '1'):
            new_value[i] = '1'
        elif (mask[i] == '0'):
            new_value[i] = binary_value[i]
        elif (mask[i] == 'X'):
            new_value[i] = 'X'

    return "".join(new_value)

def get_memory_addresses(memory_addresses, floating_address):
    if (floating_address.find('X') == -1):
        memory_addresses.append(floating_address)
    else:
        get_memory_addresses(memory_addresses, floating_address.replace('X','0', 1))
        get_memory_addresses(memory_addresses, floating_address.replace('X','1', 1))

    return memory_addresses

def part_1(input):
    mask ,address, value = 0, 0, 0
    values = {}
    for _, line in enumerate(input):
        if (line[:4] == 'mask'):
            mask = line.split(' = ')[1]
        elif (line[:3] == 'mem'):
            address, value = get_address_and_value(line)
        
        if not (address == 0 and value == 0):
            values[address] = apply_bitmask(mask, value)
            address = 0
            value = 0
    
    print(f'Sum:{sum(values.values())}')

def part_2(input):
    mask ,address, value = 0, 0, 0
    values = {}    
    for _, line in enumerate(input):
        memory_addresses = []
        if (line[:4] == 'mask'):
            mask = line.split(' = ')[1]
        elif (line[:3] == 'mem'):
            address, value = get_address_and_value(line)
            floating_address = apply_bitmask2(mask, address)
            memory_addresses = get_memory_addresses(memory_addresses, floating_address)
            for address in memory_addresses:
                values[address] = int(value)


    
    print(f'Sum:{sum(values.values())}')

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    inputfile = open(path + '\\14input.txt', 'r')

    input = inputfile.read().splitlines()

    part_1(input)
    part_2(input)


if __name__ == '__main__':
    main()