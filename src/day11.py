import copy

def assign_rules(structure_data):
    result = []
    for row_number, row in enumerate(structure_data):
        result_row = copy.deepcopy(row)
        for column, seat in enumerate(row):
            if seat == 'L':
                adjacents = get_adjacent(row_number, column, structure_data)
                if '#' not in adjacents:
                    result_row[column] = '#'
            if seat == '#':
                adjacents = get_adjacent(row_number, column, structure_data)
                if count_occupied_seats(adjacents) >= 4:
                    result_row[column] = 'L'
        result.append(result_row)
    return(result)

def count_occupied_seats(row):
    count = 0
    for seat in row:
        if seat == '#':
            count += 1
    return count

def get_adjacent(row_number, column, structure_data):
    try:
        adjacent_upper_row = []
        adjacent_lower_row = []
        result = []
        from_column = max(0,column - 1)
        to_column = min(len(structure_data[0]), column + 2)

        if row_number - 1 >= 0:
            adjacent_upper_row = structure_data[row_number - 1][from_column:to_column]
            result.extend(adjacent_upper_row)

        if column - 1 < 0:
            adjacent_same_row = [structure_data[row_number][to_column - 1]]
        elif column + 1 == len(structure_data[0]):
            adjacent_same_row = [structure_data[row_number][from_column]]
        else:
            adjacent_same_row = [structure_data[row_number][from_column], structure_data[row_number][to_column - 1]]
        result.extend(adjacent_same_row)

        if row_number + 1 < len(structure_data[:]):
            adjacent_lower_row = structure_data[row_number + 1][from_column:to_column]
            result.extend(adjacent_lower_row)
        return result
    except :
        print(row_number)
    

def compare_data(previous, new):
    previous_str = ''.join([''.join(row) for row in previous])
    after_str = ''.join([''.join(row) for row in new])
    return previous_str == after_str


with open("data/day11.txt") as file:
    data = file.read()
    rows = data.split('\n')
    structure_data = []
    for row_number, row in enumerate(rows):
        structure_data.append([seat for seat in row])
    different = True
    previous_data = copy.deepcopy(structure_data)
    count_app = 0
    after_rules = assign_rules(previous_data)
    while different:
        count_app += 1
        after_rules = assign_rules(previous_data)
        if compare_data(previous_data, after_rules):
            different = False
        previous_data = copy.deepcopy(after_rules)
    occupied_seats_total = 0
    for row in after_rules:
        # print(row)
        occupied_seats_total += count_occupied_seats(row)
    print(occupied_seats_total)
    
