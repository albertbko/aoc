import os
import time

def get_valid_ranges(rules):
    valid_ranges = []

    for rule in rules:
        ranges = rule.split(':')[1].split('or')
        for range in ranges:
            numbers = range.split('-')
            lower = int(numbers[0])
            upper = int(numbers[1])
            valid_ranges.append(tuple((lower,upper)))
    
    return valid_ranges

def is_valid(valid_ranges, value):
    for i in range(0, len(valid_ranges), 2):
        if (value >= valid_ranges[i][0] and value <= valid_ranges[i][1]) or (value >= valid_ranges[i+1][0] and value <= valid_ranges[i+1][1]):
            return True
    return False

def find_field(rules, valid_tickets):
    # convert tickets to ints
    tickets = []
    for valid_ticket in valid_tickets:
        tickets.append([int(x) for x in valid_ticket.split(',')])

    columns = []
    for i in range(len(tickets[0])):
        columns.append(i)

    fields = {}
    for rule in rules:
        field = rule.split(':')[0]
        valid_ranges = []
        ranges = rule.split(':')[1].split('or')
        for valid_range in ranges:
            numbers = valid_range.split('-')
            lower = int(numbers[0])
            upper = int(numbers[1])
            valid_ranges.append(tuple((lower,upper)))
        # try every column of ticket
        for col in columns:
            for row in tickets:
                if not (is_valid(valid_ranges, row[col])):
                    break
                elif (row == tickets[-1]):
                    possible = fields.get(field, [])
                    possible.append(col)
                    fields[field] = possible

    # process possible matches to a unique match
    matched_fields = {}
    matched_cols = []
    matching = True
    while (matching):
        for field in fields:
            cols = fields.get(field, [])
            
            # remove any matched columns
            for matched_col in matched_cols:
                try:
                    cols.remove(matched_col)
                except:
                    pass

            if (len(cols) == 1):
                matched_fields[field] = cols[0]
                # keep track of matched columns so they can be removed from other fields
                matched_cols.append(cols[0])
                
        if (len(matched_fields)) == 20:
            matching = False


    return matched_fields

def part1(rules, nearby_tickets):
    valid_ranges = get_valid_ranges(rules)

    scan_error_rate = 0
    for ticket in nearby_tickets:
        values = [int(x) for x in ticket.split(',')]
        for value in values:
            if not (is_valid(valid_ranges, value)):
                scan_error_rate += value
                break

    return scan_error_rate

def part2(rules, my_ticket, nearby_tickets):
    valid_ranges = get_valid_ranges(rules)

    valid_tickets = []
    for ticket in nearby_tickets:
        values = [int(x) for x in ticket.split(',')]
        for value in values:
            if not (is_valid(valid_ranges, value)):
                break
            elif (value == values[-1]):
                valid_tickets.append(ticket)

    fields = find_field(rules, valid_tickets)

    my_ticket = [int(x) for x in my_ticket[1].split(',')]

    return my_ticket[fields['departure location']] * my_ticket[fields['departure station']] * my_ticket[fields['departure platform']] * my_ticket[fields['departure track']] * my_ticket[fields['departure date']] * my_ticket[fields['departure time']]

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    inputfile = open(path + '\\16input.txt', 'r')
    input = inputfile.read().split('\n\n')
    rules = input[0].splitlines()
    my_ticket = input[1].splitlines()
    nearby_tickets = input[2].splitlines()[1:]

    start = time.time()
    print(f'Answer:{part1(rules, nearby_tickets)}')
    print('=== Runtime %s seconds ===' % (time.time() - start))

    start = time.time()
    print(f'Answer:{part2(rules, my_ticket, nearby_tickets)}')
    print('=== Runtime %s seconds ===' % (time.time() - start))


if __name__ == '__main__':
    main() 