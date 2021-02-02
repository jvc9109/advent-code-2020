import re


def solve_parenthesis(operation):
    result = None
    skip_to = -1
    for idx, item in enumerate(operation):
        if skip_to >= 0:
            skip_to -= 1
            continue
        if item == ')':
            break
        if item == '(':
            temp_result, skip_to = solve_parenthesis(operation[idx+1:])
            if not result:
                result = temp_result
            else:
                result = eval(f'{result}{action}{temp_result}')
        else:
            if item in ['+', '*']:
                action = item
            elif not result:
                result = item
            elif item == '(':
                temp_result, skip_to = solve_parenthesis(operation[idx+1:])
                result = eval(f'{result}{action}{temp_result}')
            elif item not in ['(', ')']:
                result = eval(f'{result}{action}{item}')
    return result, idx


def calculate_value(operation):
    result = None
    action = None
    skip_to = -1
    for idx, item in enumerate(operation):
        if skip_to >= 0:
            skip_to -= 1
            continue
        if item in ['+', '*']:
            action = item
        elif item == '(':
            temp_result, skip_to = solve_parenthesis(operation[idx+1:])
            if not result:
                result = temp_result
            else:
                result = eval(f'{result}{action}{temp_result}')
        elif not result:
            result = item
        elif item not in ['(', ')']:
            result = eval(f'{result}{action}{item}')
    return result

with open('data/day18.txt') as file:
    operations = file.read().split('\n')
    total = 0
    for line in operations:
        line = line.replace(' ', '')
        result = calculate_value(line)
        print(f'the result from {line} is {result}')
        total += result
    print(f'the final result is {total}')