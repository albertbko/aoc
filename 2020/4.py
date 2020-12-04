import os

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\4input.txt', 'r')

input = inputfile.read().split('\n\n')

# Part 1
#required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
#def validate_passport(password):
#    fields = password.split()
#
#    for required in required_fields:
#        if not any(required in s for s in fields):
#            return False
#    
#    return True
#
#valid = 0
#for i, passport in enumerate(input):
#    if(validate_passport(passport)):
#        valid += 1
#
#print(valid)

# Part 2
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def validate_height(field):
    if (len(field) == 5 and field[3] == 'c' and field[4] == 'm'):
        num = int(field.split('c')[0])
        if (num >= 150 and num <= 193):
            return True

    if (len(field) == 4 and field[2] == 'i' and field[3] == 'n'):
        num = int(field.split('i')[0])
        if (num >= 59 and num <= 76):
            return True

    return False

def validate_haircolour(field):
    #valid_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    valid_chars = set('0123456789abcdef')
    try:
        if (len(field.split('#')[1]) == 6):
            if all(char in valid_chars for char in field.split('#')[1]):
                return True
        return False
    except:
        return False

def validate_ecl(field):
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if any(ecl in field for ecl in valid_ecl):
        return True

    return False

def validate_pid(field):
    valid_chars = set('0123456789')
    try:
        if (len(field) == 9):
            if all(char in valid_chars for char in field):
                return True
        return False
    except:
        return False

def validate_passport(password):
    fields = password.split()

    for required in required_fields:
        if not any(required in s for s in fields):
            return False

    for field in fields:
        split_field = field.split(':')

        if (split_field[0] == 'byr'):
             if not (int(split_field[1]) >= 1920 and int(split_field[1]) <= 2002):
                 return False
        if (split_field[0] == 'iyr'):
             if not (int(split_field[1]) >= 2010 and int(split_field[1]) <= 2020):
                 return False
        if (split_field[0] == 'eyr'):
             if not (int(split_field[1]) >= 2020 and int(split_field[1]) <= 2030):
                 return False
        if (split_field[0] == 'hgt'):
            if not (validate_height(split_field[1])):
                return False
        if (split_field[0] == 'hcl'):
            if not (validate_haircolour(split_field[1])):
                return False
        if (split_field[0] == 'ecl'):
            if not (validate_ecl(split_field[1])):
                return False
        if (split_field[0] == 'pid'):
            if not (validate_pid(split_field[1])):
                return False
    
    return True

valid = 0
for i, passport in enumerate(input):
    if (validate_passport(passport)):
        valid += 1

print(valid)