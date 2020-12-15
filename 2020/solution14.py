with open('input/input14.txt') as f:
    program = f.read().split('mask = ')

def getValues(mask, ops):
    res = {}
    xorBits = 0
    andBits = 0
    for idx in range(len(mask)):
        if mask[idx] == '1':
            xorBits += 2**idx
            andBits += 2**idx
        elif mask[idx] == 'X':
            andBits += 2**idx
    for op in ops:
        idx = int(op.split(']')[0][4:])
        val = int(op.split()[-1])
        res[idx] = (val | xorBits) & andBits
    return res

def part1():
    init = {}
    for group in program[1:]:
        mask, *ops = group.strip().split('\n')
        init.update(getValues(mask[::-1], ops))
    return sum(init.values())

def getValues2(mask, ops):
    res = {}
    for op in ops:
        opIdx = int(op.split(']')[0][4:])
        opVal = int(op.split()[-1])
        res[opVal] = [opIdx]
        for idx in range(len(mask)):
            if mask[idx] == '1':
                for i in range(len(res[opVal])):
                    res[opVal][i] = res[opVal][i] | 2**idx
            elif mask[idx] == 'X':
                for i in range(len(res[opVal])):
                    res[opVal].append(res[opVal][i] | 2**idx)
                    res[opVal][i] = res[opVal][i] & ~2**idx
    return res

def part2():
    init = {}
    for group in program[1:]:
        mask, *ops = group.strip().split('\n')
        for val, idxList in getValues2(mask[::-1], ops).items():
            for idx in idxList:
                init[idx] = val
    return sum(init.values())

print('Part 1:', part1())
print('Part 2:', part2())