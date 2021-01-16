
def problem_optimized(numbers, max_turns):
    turn = 1
    spoken_numbers = {}
    age = 0
    firsts_numbers = len(numbers)

    for index, number in enumerate(numbers):
        spoken_numbers[number] = [index]
    last_spoken_number = numbers[-1]
    for turn in range(firsts_numbers, max_turns):
        player_will_say = 0
        said_numbers = spoken_numbers.keys()
        if len(spoken_numbers[last_spoken_number]) > 1:
            player_will_say = spoken_numbers[last_spoken_number][0] - spoken_numbers[last_spoken_number][1]
        if len(spoken_numbers[last_spoken_number]) > 1000:
            spoken_numbers[last_spoken_number] = spoken_numbers[last_spoken_number][:1]
        if player_will_say in said_numbers:     
            spoken_numbers[player_will_say].insert(0,turn)
        else:
            spoken_numbers[player_will_say] = [turn]
        last_spoken_number = player_will_say
    print(last_spoken_number)

def problem_1(numbers, max_turns):
    turn = 1
    spoken_numbers = {}
    age = 0
    firsts_numbers = len(numbers)
    while turn <= max_turns:
        if turn - 1 < firsts_numbers:
            spoken_numbers[numbers[turn-1]] = [turn]
            player_says = (turn, numbers[turn-1])
        else:
            turn_said_last_spoken, last_spoken_number = player_says
            player_will_say = (turn, 0)
            said_numbers = spoken_numbers.keys()
            if last_spoken_number in said_numbers:
                if len(spoken_numbers[last_spoken_number]) > 1:
                    player_will_say = (turn, turn_said_last_spoken - spoken_numbers[last_spoken_number][-2])
            if player_will_say[1] in said_numbers:     
                spoken_numbers[player_will_say[1]].append(turn)
            else:
                spoken_numbers[player_will_say[1]] = [turn]
            player_says = player_will_say
        turn += 1
    print(player_says)
    return spoken_numbers
            

with open("data/day15.txt") as file:
    starting_numbers = [int(number) for number in file.read().split(',')]
    problem_1(starting_numbers, 30000000)