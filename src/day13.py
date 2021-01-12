import numpy as np

def problem_1(arrival, buslines):
    waiting = True
    mins_waiting = 0
    while waiting:
        f = lambda x: (arrival_min + mins_waiting) % x
        result, = np.where(f(buslines) == 0)
        if len(result) > 0:
            result_bus = buslines[result[0]]
            break
        mins_waiting += 1
        
    print(result_bus*mins_waiting)


def get_steps_array(buslines):
    step = 0
    steps_arr = []
    for bus_line in buslines.split(','):
        if bus_line != 'x':
            steps_arr.append(step)
        step += 1
    return steps_arr

def extended_gdc(a, b):
    t = 1
    s = 0

    old_t = 0
    old_s = 1
    
    a1 = a
    b1 = b

    while b1 > 0:
        quotient = a1 // b1
        a1, b1 = b1, a1 - quotient*b1
        s, old_s = old_s, s - quotient*old_s
        t, old_t = old_t, t - quotient*old_t

    return t,s

def problem_2(buslines, buslines_parsed):
    divs = []
    t = buslines.split(',')
    for i in range(len(t)):
        if t[i] == 'x':
            continue
 
        t[i] = int(t[i]) 
 
        k = i
        k %= t[i]
        k = t[i] - k
        k %= t[i]
 
        divs.append([int(t[i]), k])
    print(divs)
    while len(divs) > 1:
        n1, a1 = divs[-1]
        n2, a2 = divs[-2]
 
        divs.pop()
        divs.pop()
        m1, m2 = extended_gdc(n1, n2)
        x = a1*m2*n2 + a2*m1*n1
        x %= n1*n2
 
        if x < 0:
            x += n1*n2
        divs.append([n1*n2, x])
        print(divs)
    print(divs[0][1])

with open("data/day13.txt") as file:
    [arrival, bus_lines] = file.read().splitlines()
arrival_min = int(arrival)
bus_lines_parsed = [int(bus_line) for bus_line in bus_lines.split(',') if bus_line != 'x']
# problem_1(arrival_min, np.array(bus_lines_parsed))
problem_2(bus_lines, bus_lines_parsed)



