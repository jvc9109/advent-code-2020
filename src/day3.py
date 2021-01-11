def count_trees(lines, slope_right, slope_down):
    tree_mark = '#'
    current_position = 0
    tree_count = 0
    scenario_length = len(lines[0])
    for idx in range(0,len(lines), slope_down):
        if lines[idx][current_position] == tree_mark:
            tree_count += 1
        current_position = (current_position + slope_right) % scenario_length
    print(f'There are {tree_count} trees in the path with slope ({slope_right}, {slope_down})')
    return tree_count

with open("data/day3.txt") as file:
    data = file.read()
    lines = data.split('\n')
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    result = 1
    for slope_x, slope_y in slopes:
        trees = count_trees(lines, slope_x, slope_y)
        result = result*trees
    print(f'the final answer is {result}')