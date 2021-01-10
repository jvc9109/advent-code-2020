import copy

def process_instrucctions(idx, instruction_set, accu):
    inst_processing = instruction_set.split(' ')
    instruction_action = inst_processing[0]
    instruction_value = int(inst_processing[1])
    if instruction_action == 'nop':
        idx += 1
    if instruction_action == 'acc':
        accu += instruction_value
        idx += 1
    if instruction_action == 'jmp':
        idx += instruction_value
    
    return idx, instruction_action, accu

def process_instrucctions_backwards(idx, instruction_set, accu):
    inst_processing = instruction_set.split(' ')
    instruction_action = inst_processing[0]
    instruction_value = int(inst_processing[1])
    if instruction_action == 'nop':
        idx -= 1
    if instruction_action == 'acc':
        accu += instruction_value
        idx -= 1
    if instruction_action == 'jmp':
        idx -= instruction_value
    
    return idx, instruction_action, accu

def get_last_acc(instruction_set):
    accu = 0
    idx = 0
    processing = True
    had_loop = False
    instruction_len = len(instruction_set)
    idx_visited = []
    while processing:
        if idx in idx_visited:
            idx_to_change = idx_visited[-1]
            had_loop = True
            break
        idx_visited.append(idx)
        idx, instruction_action, accu = process_instrucctions(idx, instruction_set[idx], accu)
        if instruction_len <= idx or idx < 0:
            processing = False
    return accu, had_loop


def get_acc_with_debug(instruction_set):
    accu = 0
    idx = 0
    idx_visited = []
    processing = True
    instruction_len = len(instruction_set)
    idx_visited = []
    while processing:
        if 'jmp' in instruction_set[idx] or 'nop' in instruction_set[idx]:
            new_instructions_set = copy.deepcopy(instruction_set)
            new_instructions_set[idx] = debug_instrucction(instruction_set[idx])
            accu_debuged, had_loop = get_last_acc(new_instructions_set)
            if not had_loop:
                accu = accu_debuged
                print(f'instruction changed {instruction_set[idx]} with idx: {idx}')
                processing = False
        idx += 1
    return accu



def debug_instrucction(instruction_set):
    inst_processing = instruction_set.split(' ')
    instruction_action = inst_processing[0]
    instruction_value = inst_processing[1]
    if instruction_action == 'nop':
        return ' '.join(['jmp', instruction_value])
    if instruction_action == 'jmp':
        return ' '.join(['nop', instruction_value])


with open("data/day8.txt") as file:
    data = file.read()
    instruction_set = data.split('\n')
    print(f'last accu {get_last_acc(instruction_set)[0]}')
    print(f'output debuged {get_acc_with_debug(instruction_set)}')

    

