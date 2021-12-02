with open('day1.txt') as fd:
    data = list(map(int, fd.readlines()))

def part1():
    return sum([a > b for a, b in zip(data[1:], data)])

def part2():
    windows = list(map(sum, zip(data, data[1:], data[2:])))
    return sum([a > b for a, b in zip(windows[1:], windows)])

print(f'Part 1: {part1()} measurements are larger.')
print(f'Part 2: {part2()} windows are larger.')

