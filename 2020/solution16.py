import re

with open('input/input16.txt') as f:
    blobs = f.read().split('\n\n')

fields = blobs[0].split('\n')
myTicket = blobs[1].split('\n')[1]
nearbyTickets = blobs[2].split('\n')[1:]

ranges = {}
for field in fields:
    name, *vals = field.split(': ')
    rangeRule = re.compile(r'(\d+)-(\d+) or (\d+)-(\d+)')
    rangeLimits = rangeRule.findall(vals[0])
    ranges[name] = list(map(int, rangeLimits[0]))

def isValid(v):
    validRanges = []
    for n, r in ranges.items():
        if (v >= r[0] and v <= r[1]) or (v >= r[2] and v <= r[3]):
            validRanges.append(n)
    return validRanges

def part1():
    err = 0
    for ticket in nearbyTickets:
        for value in list(map(int, ticket.split(','))):
            if not isValid(value):
                err += value
    return err

def part2():
    validRanges = {}
    for ticket in nearbyTickets:
        tktVals = list(map(int, ticket.split(',')))
        for idx in range(len(tktVals)):
            curRanges = isValid(tktVals[idx])
            if curRanges:
                if not idx in validRanges:
                    validRanges[idx] = set(curRanges)
                else:
                    validRanges[idx] = validRanges[idx].intersection(set(curRanges))
    myVals = {}
    myTicketVals = list(map(int, myTicket.split(',')))
    while len(myVals) < len(myTicketVals):
        for idx, names in validRanges.items():
            if len(names) == 1:
                name = names.pop()
                myVals[name] = myTicketVals[idx]
                validRanges.pop(idx)
                for idx2 in validRanges.keys():
                    validRanges[idx2].remove(name)
                break
    total = 1
    for name, val in myVals.items():
        if name.startswith('departure'):
            total *= val
    return total

print('Part 1:', part1())
print('Part 2:', part2())