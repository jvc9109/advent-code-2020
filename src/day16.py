import re
import copy


def check_number_in_rule(rule: list, number: int) -> bool:
    result = False
    for rule_range in rule:
        if rule_range[0] <= number <= rule_range[1]:
            result = True
            break
    return result

def get_valid_tickets(nearby_tickets, rules):
    error_rate = 0
    valid_tickets = copy.deepcopy(nearby_tickets)
    for ticket in nearby_tickets:
        is_ticket_valid = True
        for number in ticket:
            if not is_ticket_valid:
                break
            for rule in rules:
                if check_number_in_rule(rules[rule], number):
                    break
            else:
                error_rate += number
                is_ticket_valid = False
                valid_tickets.remove(ticket)
    return valid_tickets

def guess_option(tickets, rules):
    is_rule_set = False
    position_check = 0
    result =[]
    while not is_rule_set:
        possible_rules = list(rules.keys())

        for ticket in tickets:
            for rule in rules:
                if rule not in possible_rules:
                    continue
                if rule in result:
                    possible_rules.remove(rule)
                    continue
                if not check_number_in_rule(rules[rule], ticket[position_check]):
                    possible_rules.remove(rule)
            if len(possible_rules) == 1:
                for idx, previous_result in enumerate(result):
                    if type(previous_result) == type([]) and possible_rules[0] in previous_result:
                        previous_result.remove(possible_rules[0])
                        if len(previous_result) == 1:
                            result[idx] =  previous_result[0]
                            result = clean_results(previous_result[0], result)
                    else:
                        result = clean_results(previous_result, result)
                result.append(possible_rules[0])
                position_check += 1
                break
        else:
            result.append(possible_rules)
            position_check += 1
            continue
        if len(result) == len(nearby_tickets[0]):
            is_rule_set = True
    return result

def clean_results(rule_to_check, set_possible_rules):
    for idx, possible_results in enumerate(set_possible_rules):
        if type(possible_results) == type([]) and rule_to_check in possible_results:
            possible_results.remove(rule_to_check)
            if len(possible_results) == 1:
                set_possible_rules[idx] =  possible_results[0]
                set_possible_rules = clean_results(possible_results[0], set_possible_rules)
    return set_possible_rules

def obtain_rules(rules_str):
    rules_pattern = r'(.*):\s+([0-9]+)-([0-9]+)\s+or\s+([0-9]+)-([0-9]+)'
    rules = {}

    for rule in rules_str:
        rule_name, from_one, to_one, from_two, to_two = re.findall(rules_pattern, rule)[0]
        valid_range = [(int(from_one), int(to_one)), (int(from_two), int(to_two))]
        rules[rule_name] = valid_range
    return rules


current_ticket = [53,101,83,151,127,131,103,61,73,71,97,89,113,67,149,163,139,59,79,137]

with open("data/day16.txt") as file:
    nearby_tickets = [ list(map(lambda x: int(x), numbers.split(','))) for numbers in file.read().split('\n')]

with open('data/day16_rules.txt') as file:
    rules_str = file.read().split('\n')


rules = obtain_rules(rules_str)

valid_tickets = get_valid_tickets(nearby_tickets, rules)

rule_orders = guess_option(valid_tickets, rules)

multip = 1

for idx, rule_name in enumerate(rule_orders):
    if 'departure' in rule_name:
        multip *= current_ticket[idx]

print(multip)
