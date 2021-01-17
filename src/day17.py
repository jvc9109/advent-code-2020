import re
from collections import defaultdict, deque

def get_neighbours(position):
    neighbours = set()
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if x==0 and y==0 and z==0:
                    continue
                neighbours.add((position[0] + x, position[1] + y, position[2] + z))
    return neighbours

def count_active_neighbours(possible_neighbours, points):
    return [x for x in possible_neighbours if x in points]

def read_region(input_list: list) -> dict:
    points_active = set()
    for x, line in enumerate(input_list):
        for y, state in enumerate(line):
            if state == '#':
                points_active.add((x,y,0))
    return points_active

def read_region_4_dim(input_list):
    points_active = set()
    for x, line in enumerate(input_list):
        for y, state in enumerate(line):
            if state == '#':
                points_active.add((x,y,0,0))
    return points_active

def get_neighbours_4_dim(position):
    neighbours = set()
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for w in range(-1, 2):
                    if x==0 and y==0 and z==0 and w==0:
                        continue
                    neighbours.add((position[0] + x, position[1] + y, position[2] + z, position[3] + w))
    return neighbours

def problem_1(active_points):
    for cycle in range(6):
        new_points = set()
        for point in active_points:
            neighbours = get_neighbours(point)
            count_active_points = len(count_active_neighbours(neighbours, active_points))
            if count_active_points == 2 or count_active_points == 3:
                new_points.add(point)
            for neighbour in neighbours:
                if len(count_active_neighbours(get_neighbours(neighbour), active_points)) == 3:
                    new_points.add(neighbour)
        active_points = new_points
    print(len(active_points))

def problem_2(active_points):
    for cycle in range(6):
        new_points = set()
        for point in active_points:
            neighbours = get_neighbours_4_dim(point)
            count_active_points = len(count_active_neighbours(neighbours, active_points))
            if count_active_points == 2 or count_active_points == 3:
                new_points.add(point)
            for neighbour in neighbours:
                if len(count_active_neighbours(get_neighbours_4_dim(neighbour), active_points)) == 3:
                    new_points.add(neighbour)
        active_points = new_points
    print(len(active_points))

with open('data/day17.txt') as file:
    intial_str = file.read().split('\n')
    active_points = read_region(intial_str)
    active_points_4d = read_region_4_dim(intial_str)
    problem_1(active_points)
    problem_2(active_points_4d)

