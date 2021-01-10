def rules_mapper(lines):
    colors_saw = []
    result = {}
    for rule_str in lines:
        rule_first_split = rule_str.split('contain')
        rule_bag = ' '.join(rule_first_split[0].split(' ')[:2])
        if rule_first_split[1].lstrip() != 'no other bags.':
            current_bag_hold = []
            result[rule_bag] = []
            for rule in rule_first_split[1].split(','):
                rule_components = rule.lstrip().split(' ')
                number_bags = rule_components[0]
                bag_color = ' '.join(rule_components[1:3])
                result[rule_bag].append(bag_color)
                if bag_color in result.keys():
                    result[rule_bag].extend(result[bag_color])
                colors_saw.append(bag_color)
            if rule_bag in colors_saw:
                for bigger_bag in result:
                    if rule_bag in result[bigger_bag]:
                        result[bigger_bag].extend(result[rule_bag])
    return result

def rules_mapper_2(lines):
    result = {}
    for rule_str in lines:
        rule_first_split = rule_str.split('contain')
        rule_bag = ' '.join(rule_first_split[0].split(' ')[:2])
        result[rule_bag] = []
        if rule_first_split[1].lstrip() != 'no other bags.':
            for rule in rule_first_split[1].split(','):
                rule_components = rule.lstrip().split(' ')
                number_bags = int(rule_components[0])
                bag_color = ' '.join(rule_components[1:3])
                result[rule_bag].append({'color': bag_color, 'number': number_bags})
    return result

def get_number_bags_from_color(color, rules_v2):
    total_amount_bags = 0
    if (len(rules_v2[color]) == 0):
        return 0
    for prim_bags in rules_v2[color]:
        total_current_color = 0
        bag_color = prim_bags['color']
        total_current_color += prim_bags['number']
        total_from_recursive = get_number_bags_from_color(bag_color, rules_v2)
        total_current_color += prim_bags['number']*total_from_recursive
        total_amount_bags += total_current_color
    return total_amount_bags

with open("../data/day7.txt") as file:
    data = file.read()
    lines = data.split('\n')
    rules_down_shiny_gold = rules_mapper(lines)
    how_many_can_shiny = 0
    for rule_bag in rules_down_shiny_gold:
        if 'shiny gold' in rules_down_shiny_gold[rule_bag]:
            how_many_can_shiny += 1
    
    print(how_many_can_shiny)
    rules_v2 = rules_mapper_2(lines)
    print(get_number_bags_from_color('shiny gold', rules_v2))
    
