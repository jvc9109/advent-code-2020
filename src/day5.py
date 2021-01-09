def calculate_seat(seat_string):
    current_row = (0, 127)
    current_column = (0, 7)
    current_row_distance = 63
    current_column_distance = 3
    for i in range(0,7):
        if seat_string[i] == 'F':
            current_row = (current_row[0], current_row[1] - current_row_distance - 1)
        elif seat_string[i] == 'B':
            current_row = (current_row[0] + current_row_distance + 1 , current_row[1])
        current_row_distance = (current_row_distance - 1)/2
    for i in range(7,10):
        if seat_string[i] == 'L':
            current_column = (current_column[0], current_column[1] - current_column_distance - 1)        
        elif seat_string[i] == 'R':
            current_column = (current_column[0] + current_column_distance + 1 , current_column[1])
        current_column_distance = (current_column_distance - 1)/2
    return (current_row[0], current_column[0])


with open("../data/day5.txt") as file:
    seats = file.read().split('\n')
    seat_ids = []
    for seat in seats:
        (row, column) = calculate_seat(seat)
        seat_ids.append((row*8) + column)
        print(f'row: {row} column: {column}')
    print(max(seat_ids))