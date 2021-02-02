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


def calc_operation(matchobj):
    sum_operations = matchobj.group(0).replace('(', '').replace(')', '').split('*')
    sum_results = []
    for sum_operation in sum_operations:
        sum_results.append(str(eval(sum_operation)))
    
    final_operation = '*'.join(sum_results)

    return str(eval(final_operation))

def calc_final(operation):
    sum_operations = operation.split('*')
    sum_results = []
    for sum_operation in sum_operations:
        sum_results.append(str(eval(sum_operation)))
    
    final_operation = '*'.join(sum_results)

    return eval(final_operation)

def problem2(operation):
    pattern = r'\([^\(\)]+\)'
    inner_operations = re.sub(pattern, calc_operation, operation)
    if '(' in inner_operations:
        inner_operations = str(problem2(inner_operations))
    
    return calc_final(inner_operations)


with open('data/day18.txt') as file:
    operations = file.read().split('\n')
    total = 0
    for line in operations:
        line = line.replace(' ', '')
        result = calculate_value(line)
        result2 = problem2(line)
        print(f'the result from {line} is {result2}')
        total += result2

    print(f'the final result is {total}')