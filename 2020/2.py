import os

path = os.path.abspath(os.path.dirname(__file__))
inputfile = open(path + '\\2input.txt', 'r')

input = inputfile.read().splitlines()
#print(input)

# Part 1
#def validate_password(password):
#    #print(password)
#    row = password.split(' ')
#    min = int(row[0].partition('-')[0])
#    max = int(row[0].partition('-')[2])
#    letter = row[1][0]
#    password = row[2]
#    count = password.count(letter)
#
#    if (count >= min and count <= max):
#        return True
#    
#    return False

# Part 2
def validate_password(password):
    #print(password)
    row = password.split(' ')
    pos_1 = int(row[0].partition('-')[0]) - 1
    pos_2 = int(row[0].partition('-')[2]) - 1
    letter = row[1][0]
    password = row[2]

    if (len(password) < pos_2):
        return False
    if ((password[pos_1] == letter and password[pos_2] != letter) or (password[pos_1] != letter and password[pos_2] == letter)):
        return True
    
    return False

num_valid_passwords = 0
for i, entry in enumerate(input):    
    if (validate_password(entry)):
        num_valid_passwords += 1

print(num_valid_passwords)