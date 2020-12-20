#import os
#
#def make_rulebook(rules):
#    rule_dict = {}
#    for rule in rules:
#        split = rule.split(':')
#        rule_dict[split[0]] = split[1].strip()
#
#    return rule_dict
#
#def match(rule_dict, rule_number, message, index):
#    rule = rule_dict.get(rule_number)
#    matched = False
#    #print(f'Rule[{rule_number}]: {rule}')
#    if (rule == '"a"' or rule == '"b"'):
#        if (message[index] == rule.replace('"', '')):
#            #print(f'matched {message} upto {message[:index]}')
#            index += 1
#            return True, index
#        else:
#            return False, index
#
#    if ('|' in rule):
#        rules = rule.split(' | ')
#        for rule in rules:
#            starting_index = index
#            matched = False
#            subrules = rule.split(' ')
#            for subrule in subrules:
#                matched, index = match(rule_dict, subrule, message, index)
#                if not (matched):
#                    break
#            if (matched):
#                return True, index
#            else:
#                index = starting_index
#    else:
#        rules = rule.split(' ')
#        starting_index = index
#        for rule in rules:
#            matched, index = match(rule_dict, rule, message, index)
#            if not (matched):
#                break
#        if (matched):
#            return True, index
#        else:
#            index = starting_index
#    
#    if (matched == True and index == len(message)):
#    #if (matched == True and index == 24):
#        return True, index
#    else:
#        return False, index
#
#
#def part1(rules, messages):
#    rule_dict = make_rulebook(rules)
#    matches = 0
#    for message in messages:
#        #print(f'Matching:{message}')
#        matched, _ = match(rule_dict, '0', message, 0)
#        if (matched):
#            print(f'Match:{message}')
#            matches += 1
#    print(matches)
#
#def main():
#    path = os.path.abspath(os.path.dirname(__file__))
#    inputfile = open(path + '\\19input.txt', 'r')
#    input = inputfile.read().split('\n\n')
#    rules = input[0].splitlines()
#    messages = input[1].splitlines()
#
#    part1(rules, messages)
#
#
#if __name__ == '__main__':
#    main()

# not my solution.
# from: https://github.com/Dpalme/Advent-Of-Code/blob/master/2020/day19.py
from re import match
from functools import lru_cache
from sys import stdout
rls = {}


@lru_cache(137)
def cmp(ind, dpth=0):
    curr = rls[ind]
    return ('' if dpth > 4 else (
            curr[1] if '"' in curr else
            (f'''({"|".join([''.join([cmp(i) if i != ind
                                      else f'({cmp(ind, dpth+1)})'  
                                      for i in prt.split()])
                             for prt in curr.split('|')])})''' if '|' in curr
             else r''.join([cmp(i) for i in curr.split()]))))


def first_part(exps):
    return sum([match('^'+cmp('0')+'$', exp) is not None for exp in exps])


def second_part(exps):
    rls['8'], rls['11'] = '42 | 42 8', '42 31 | 42 11 31'
    return sum([match('^'+cmp('0')+'$', exp) is not None for exp in exps])


with open('19input.txt', 'r') as inp:
    inp_str = inp.read().split('\n\n')
    rls, exps = {exp[:exp.find(':')]: exp[exp.find(':') + 2:]
                 for exp in inp_str[0].split('\n')}, inp_str[1].split('\n')
    stdout.write(f'Day 19\nFirst part: {first_part(exps)}\n')
    cmp.cache_clear()
    stdout.write(f'Second part: {second_part(exps)}\n')