def get_jumps_count(adapters):
    diff_counter = {
        1: 0,
        2: 0,
        3: 0
    }

    current_out_power = 0
    for adapter in adapters[1:]:
        diff_counter[adapter - current_out_power] += 1
        current_out_power = adapter

    return diff_counter

def get_differences(adapters):
    differences = []
    for idx in range(1,len(adapters)):
        differences.append(adapters[idx] - adapters[idx-1])
    return differences

def get_branches_number(adapters):
    differences = get_differences(adapters)
    ones_chained = []
    count_ones = 0
    print(differences)
    for diff in differences:
        if diff == 3:
            if count_ones:
                ones_chained.append(count_ones)
            count_ones = 0
        else:
            count_ones += 1

    branches = 1
    for count_ones in ones_chained:
        if count_ones == 2:
            branches *= 2
        elif count_ones == 3:
            branches *= 4
        elif count_ones == 4:
            branches *= 7
    return branches

with open("data/day10.txt") as file:
    data = file.read()
    adapters = [int(i) for i in data.split('\n')]
    adapters.sort()
    adapters.insert(0,0)
    device_out = max(adapters) + 3
    adapters.append(device_out)
    diff_counter = get_jumps_count(adapters)
    print(diff_counter[1]*diff_counter[3])
    print(adapters)
    print(get_branches_number(adapters))
