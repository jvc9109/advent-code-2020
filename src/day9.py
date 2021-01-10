
def extract_numbers_to_validate(numbers, idx, preamble_length):
    return numbers[idx-preamble_length:idx]

def test_with_chain(number_to_test, seed_number, test_chain):
    difference = number_to_test - seed_number
    if difference != seed_number and difference in test_chain:
        return True
    return False

def is_valid_number(number_to_test, test_chain):
    for seed in test_chain:
        if test_with_chain(number_to_test, seed, test_chain):
            return True
    return False

def find_contigous_set(number_goal, test_chain):
    processing = True
    idx = len(test_chain) - 1
    initial_idx = len(test_chain) - 1
    candidates = []
    acc_diff = number_goal
    while processing:
        acc_diff = acc_diff - test_chain[idx]
        candidates.append(test_chain[idx])
        if acc_diff > 0:
            idx -= 1
        if acc_diff < 0:
            candidates = []
            acc_diff = number_goal
            idx = initial_idx - 1
            initial_idx -= 1
        if acc_diff == 0 and test_chain[idx] != number_goal:
            processing = False
        
    return candidates

with open("data/day9.txt") as file:
    data = file.read()
    numbers = [int(i) for i in data.split('\n')]
    preamble_length = 25
    for idx in range(preamble_length, len(numbers)):
        test_chain = extract_numbers_to_validate(numbers, idx, preamble_length)
        if not is_valid_number(numbers[idx], test_chain):
            print(f'the number {numbers[idx]} at position {idx} is not valid')
            weak_array = find_contigous_set(numbers[idx], numbers[:idx])
            print(sum(weak_array))
            print(f'the weakness array is {weak_array}')
            print(f'the weak number is {min(weak_array) + max(weak_array)}')