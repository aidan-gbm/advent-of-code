from functools import reduce

def part1(ts, buses):
    earliest = (0,2*ts)
    for off, bus in buses:
        nT = ((ts // bus) + 1) * bus
        if nT and nT < earliest[1]:
            earliest = (bus, nT)
    return earliest[0] * (earliest[1]-ts)

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def part2(buses):
    a, n = zip(*buses)
    return chinese_remainder(n, a)

with open('input/input13.txt') as f:
    ts = int(f.readline())
    buses = [(int(b[1])-b[0],int(b[1])) for b in list(enumerate(f.readline().split(','))) if b[1] != 'x']

print('Part 1:', part1(ts, buses))
print('Part 2:', part2(buses))