import copy

def overwrite(value_bit, mask_bit):
    if mask_bit == 'X':
        return value_bit
    elif mask_bit == '1': 
        return '1'
    else: 
        return '0'


def overwrite_mem_address(address_bit, mask_bit):
    if mask_bit == 'X':
        return 'X'
    elif mask_bit == '1':
        return mask_bit
    else:
        return address_bit

def apply_address_mask(mask, value):
    result = ''
    for i in range(len(mask)):
        result += overwrite_mem_address(value[i], mask[i])
    return result


def apply_mask(mask, value):
    result = ''
    for i in range(len(mask)):
        result += overwrite(value[i], mask[i])
    return result

def transform_to_bin_str(value_str, bit_len):
        value = bin(int(value_str))
        value = value.replace('0b', '')
        value_len = len(value)
        len_to_prepend = bit_len - value_len
        prepend_str = ''.join(['0' for i in range(len_to_prepend)])
        return prepend_str + value

def problem_1(instructions):
    mem = {}
    mask = ''
    bit_len = 36
    for instruction in instructions:
        [order_str, value_str] = instruction.replace(' ', '').split('=')
        if 'mask' in order_str:
            mask = value_str
        if 'mem' in order_str:
            value_correct = transform_to_bin_str(value_str, bit_len)
            value_masked = int('0b'+apply_mask(mask, value_correct), 2)
            new_instruction = '='.join([order_str, str(value_masked)])
            exec(new_instruction)
    print(sum(mem.values()))


def add_permutations(current_permutations, bit_to_flip):
    result = copy.deepcopy(current_permutations)
    for permutation in current_permutations:
        permutation[bit_to_flip] = '1'
        result.append(permutation)
    return result


def gen_permutations(mask):
    mask_permutations = []
    floating_bin_position = []
    mask_array = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            floating_bin_position.append(i)
            mask_array.append('0')
        else:
            mask_array.append(mask[i])

    permutations_count = 2**len(floating_bin_position)


    branch_a = mask_array
    branch_b = copy.deepcopy(mask_array)
    mask_permutations.append(branch_a)
    branch_b[floating_bin_position[-1]] = '1'
    mask_permutations.append(branch_b)

    for position in floating_bin_position[:-1]:
        mask_permutations = add_permutations(mask_permutations, position)
    
    permutations_str = [''.join(permutation) for permutation in mask_permutations]

    return permutations_str


def problem_2(instructions):
    mem = {}
    bit_len = 36
    for instruction in instructions:
        [order_str, value_str] = instruction.replace(' ', '').split('=')
        if 'mask' in order_str:
            mask = value_str
        if 'mem' in order_str:
            address_value_str = order_str.replace('mem[', '').replace(']','')
            address_value_correct = transform_to_bin_str(address_value_str, bit_len)
            possible_address = apply_address_mask(mask, address_value_correct)
            all_addresses = gen_permutations(possible_address)
            for address in all_addresses:
                possible_address_value = str(int('0b'+address, 2))
                instruction = f'mem[{possible_address_value}] = {value_str}'
                exec(instruction)
    print(sum(mem.values()))

with open("data/day14.txt") as file:
    instructions = file.read().splitlines()
    problem_1(instructions)
    problem_2(instructions)

            
            
