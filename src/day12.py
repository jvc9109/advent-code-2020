import numpy as np

def apply_mov(command, qty, position):
    
    if command == 'E':
        position[0] += qty
    elif command == 'W':
        position[0] -= qty
    elif command == 'N':
        position[1] += qty
    elif command == 'S':
        position[1] -= qty
    return position

def problem_1(instructions):
    ship_pos = np.array([0,0])
    direction = np.array([1,0])
    for instruction in instructions:
        command = instruction[0]
        qty = int(instruction[1:])
        if command in ['N', 'W', 'S', 'E']:
            ship_pos = apply_mov(command, qty, ship_pos)
        elif command == 'L':
            direction = handle_waypoint_rotation(direction, qty)
        elif command == 'R':
            direction = handle_waypoint_rotation(direction, -qty)
        elif command == 'F':
            ship_pos = move_to_direction(qty, direction, ship_pos)
    print(ship_pos)
    print(np.sum(np.abs(ship_pos)))


def move_to_direction(qty, way_rel_pos, ship_pos):
    return ship_pos + qty*way_rel_pos

def handle_waypoint_rotation(way_rel_pos, degrees):
    theta = np.deg2rad(degrees)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c, -s), (s, c))).astype(int)
    return R.dot(way_rel_pos.T)

def problem_2(instructions):
    ship_pos = np.array([0,0])
    way_rel_pos = np.array([10,1])

    for instruction in instructions:
        command = instruction[0]
        qty = int(instruction[1:])
        if command in ['N', 'W', 'S', 'E']:
            way_rel_pos = apply_mov(command, qty, way_rel_pos)
        elif command == 'L':
            way_rel_pos = handle_waypoint_rotation(way_rel_pos, qty)
        elif command == 'R':
            way_rel_pos = handle_waypoint_rotation(way_rel_pos, -qty)
        elif command == 'F':
            ship_pos = move_to_direction(qty, way_rel_pos, ship_pos)
    print(ship_pos)
    print(np.sum(np.abs(ship_pos)))
   

with open("data/day12.txt") as file:
    instructions = file.read().splitlines()
    problem_1(instructions)
    problem_2(instructions)