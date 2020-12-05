def getSeatId(row):
    row_min = 0
    row_max = 127
    for char in row:
        if (char == 'F'):
            row_max += ( - (row_max - row_min) // 2)
        elif (char == 'B'):
            row_min -= ( - abs(row_min - row_max) // 2)
    
    if row_min < row_max:
        row_id = row_min
    else:
        row_id = row_max

    col_min = 0
    col_max = 7
    for char in col:
        if char == 'L':
            col_max += ( - (col_max - col_min) // 2)
        elif char == 'R':
            col_min -= ( - abs(col_min - col_max) // 2)

    if col_min < col_max:
        col_id = col_min
    else:
        col_id = col_max
    
    return row_id * 8 + col_id

def findMyId(data):
    ids.sort()
    missing_tickets = []
    for x in range(data[0], data[-1] + 1):
        if x not in data:
            missing_tickets.append(x)
    return missing_tickets[len(missing_tickets) - 1]
    
if __name__ == "__main__":
    data = open("input.txt", 'r').read().split("\n")
    ids = []
    for id in data:
        row = id[:-3]
        col = id[-3:]
        ids.append(getSeatId(row))
    print("Your Ticket Id: " + str(max(ids)))
    print("Your New Ticket Id: " + str(findMyId(ids)))
        