ops = {'+': (lambda x,y: x+y), '*': (lambda x,y: x*y)}

def findEnd(expr):
    count = 0
    for idx in range(len(expr)):
        if expr[idx] == ')':
            count -= 1
        elif expr[idx] == '(':
            count += 1
        if count == 0 and expr[idx] == ')':
            return idx
    return -1

def findStart(expr):
    count = expr.find('(')
    while (expr[count+1] == '('):
        count += 1
    return count

def doMath(expr):
    start = findStart(expr)
    while start >= 0:
        end = start + findEnd(expr[start:])
        expr = expr[0:start] + str(doMath(expr[start+1:end])) + expr[end+1:]
        start = findStart(expr)
    parts = expr.split()
    total = int(parts[0])
    for idx in range(1,len(parts)-1,2):
        total = ops[parts[idx]](total, int(parts[idx+1]))
    return total

def doAdvancedMath(expr):
    total = 1
    start = findStart(expr)
    while start >= 0:
        end = start + findEnd(expr[start:])
        expr = expr[0:start] + str(doAdvancedMath(expr[start+1:end])) + expr[end+1:]
        start = findStart(expr)
    parts = expr.split(' * ')
    for part in parts:
        total2 = 0
        parts2 = part.split(' + ')
        for part2 in parts2:
            total2 += int(part2)
        total *= total2
    return total
            
def part1():
    total = 0
    with open('input/input18.txt') as f:
        for line in f.readlines():
            total += doMath(line.strip())
    return total

def part2():
    total = 0
    with open('input/input18.txt') as f:
        for line in f.readlines():
            total += doAdvancedMath(line.strip())
    return total

print('Part 1:', part1())
print('Part 2:', part2())