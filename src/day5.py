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
    seats_ordered = {key: [i for i in range(0,8)] for key in range(0,128)}
    
    for seat in seats:
        (row, column) = calculate_seat(seat)
        seat_ids.append((row*8) + column)
        seats_ordered[int(row)].remove(int(column))
    
    print(f'max id: {max(seat_ids)}')
    
    for row in seats_ordered:
        if len(seats_ordered[row]) == 1:
            candidate_id = row*8 + seats_ordered[row][0]
            if candidate_id + 1 in seat_ids and candidate_id - 1 in seat_ids:
                print(f' My seat is row {row} with seat {seats_ordered[row]} with id {candidate_id}')
