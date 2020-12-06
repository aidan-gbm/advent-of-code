def search(hi, lo, input):
    if not input:
        return hi
    elif input[0] == 'F' or input[0] == 'L':
        return search(int(hi-(hi-lo)/2), lo, input[1:])
    else:
        return search(hi, int(lo+(hi-lo)/2), input[1:])

def part1():
    highest = 0
    with open('input5.txt') as f:
        for bp in f.readlines():
            row = search(127, 0, bp[0:7])
            col = search(7, 0, bp[7:])
            highest = max(highest, row * 8 + col)
    return highest

def part2():
    seats = {}
    with open('input5.txt') as f:
        for bp in f.readlines():
            row = search(127,0,bp[0:7])
            if row not in seats:
                seats[row] = []
            seats[row].append(search(7,0,bp[7:]))
    
    for row, cols in seats.items():
        diff = {0,1,2,3,4,5,6,7} - set(cols)
        if len(diff) != 0 and row-1 in seats.keys() and row+1 in seats.keys():
            return row * 8 + diff.pop()

print(part1())
print(part2())