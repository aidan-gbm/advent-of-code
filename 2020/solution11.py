def surrounding(seats, row, col):
    count = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r < 0 or r >= len(seats) or c < 0 or c >= len(seats[0]) or (row == r and col == c):
                continue
            if seats[r][c] == '#':
                count += 1
    return count

def doRound(seats):
    newSeats, changes = ([], 0)
    for row in range(len(seats)):
        newSeats.append([])
        for col in range(len(seats[0])):
            if seats[row][col] == 'L' and surrounding(seats, row, col) == 0:
                newSeats[row].append('#')
                changes += 1
            elif seats[row][col] == '#' and surrounding(seats, row, col) > 3:
                newSeats[row].append('L')
                changes += 1
            else:
                newSeats[row].append(seats[row][col])
    return (newSeats, changes)

def part1():
    seats = []
    with open('input11.txt') as f:
        for line in f.readlines():
            seats.append(list(line.strip()))
    
    (newSeats, changes) = doRound(seats)
    while changes != 0:
        (newSeats, changes) = doRound(newSeats)
    return len([seat for rows in newSeats for seat in rows if seat == '#'])

def surrounding2(seats, row, col):
    count = 0
    # Going up
    for r in range(row-1,-1,-1):
        s = seats[r][col]
        if s == '#':
            count += 1
            break
        elif s == 'L':
            break
    # Going down
    for r in range(row+1, len(seats)):
        s = seats[r][col]
        if s == '#':
            count += 1
            break
        elif s == 'L':
            break
    # Going left
    for c in range(col-1,-1,-1):
        s = seats[row][c]
        if s == '#':
            count += 1
            break
        elif s == 'L':
            break
    # Going right
    for c in range(col+1,len(seats[0])):
        s = seats[row][c]
        if s == '#':
            count += 1
            break
        elif s == 'L':
            break
    # Going up & left
    for r, c in zip(range(row-1,-1,-1), range(col-1,-1,-1)):
        s = seats[r][c]
        if s == '#':
            count += 1
            break
        elif s == 'L':
            break
    # Going up & right
    for r, c in zip(range(row-1,-1,-1), range(col+1,len(seats[0]))):
        s = seats[r][c]
        if s == '#':
            count += 1
            break
        elif s == 'L':
            break
    # Going down & left
    for r, c in zip(range(row+1, len(seats)), range(col-1,-1,-1)):
        s = seats[r][c]
        if s == '#':
            count += 1
            break
        elif s == 'L':
            break
    # Going down & right
    for r, c in zip(range(row+1, len(seats)), range(col+1,len(seats[0]))):
        s = seats[r][c]
        if s == '#':
            count += 1
            break
        elif s == 'L':
            break
    return count

def doRound2(seats):
    newSeats, changes = ([], 0)
    for row in range(len(seats)):
        newSeats.append([])
        for col in range(len(seats[0])):
            s = seats[row][col]
            if s == 'L' and surrounding2(seats, row, col) == 0:
                newSeats[row].append('#')
                changes += 1
            elif s == '#' and surrounding2(seats, row, col) > 4:
                newSeats[row].append('L')
                changes += 1
            else:
                newSeats[row].append(s)
    return (newSeats, changes)

def part2():
    seats = []
    with open('input11.txt') as f:
        for line in f.readlines():
            seats.append(list(line.strip()))
    
    (newSeats, changes) = doRound2(seats)
    while changes != 0:
        (newSeats, changes) = doRound2(newSeats)
    return len([seat for rows in newSeats for seat in rows if seat == '#'])

print('Part 1:', part1())
print('Part 2:', part2())