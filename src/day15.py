

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
            # for turn_said, spoken_number in spoken_numbers[1:]:
            #     if last_spoken_number == spoken_number:
            #         player_says = (turn, turn_said_last_spoken - turn_said)
            #         break
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
    # problem_2(starting_numbers)