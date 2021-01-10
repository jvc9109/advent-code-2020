from collections import Counter

def problem_1(lines):
    groups_yes = []
    current_yes = []
    for line in lines:
        if line == '':
            to_append = list(set(current_yes))
            groups_yes.append(len(to_append))
            current_yes = []
        else:
            current_yes.extend([chart for chart in line])

    to_append = list(set(current_yes))
    groups_yes.append(len(to_append))
    return groups_yes


def problem_2(lines):
    group_size = 0
    current_yes = []
    groups_yes = []
    for line in lines:
        if line == '':
            yes_counter = Counter(current_yes)
            group_count = 0
            for key in yes_counter:
                if yes_counter[key] == group_size:
                    group_count += 1
            groups_yes.append(group_count)
            current_yes = []
            group_size = 0
        else:
            group_size += 1
            current_yes.extend([chart for chart in line])

    yes_counter = Counter(current_yes)
    group_count = 0
    for key in yes_counter:
        if yes_counter[key] == group_size:
            group_count += 1
    groups_yes.append(group_count)

    return groups_yes



with open("../data/day6.txt") as file:
    data = file.read()
    lines = data.split('\n')
    print(sum(problem_1(lines)))
    print(sum(problem_2(lines)))
