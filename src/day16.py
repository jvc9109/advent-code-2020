
with open("data/day16.txt") as file:
    nearby_tickets = [ numbers.split(',') for numbers in file.read().readlines()]
    print(nearby_tickets)