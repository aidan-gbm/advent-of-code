import re

with open('input8.txt') as f:
    instructions = f.readlines()
    instructions2 = instructions.copy()

ops = {'+': (lambda x,y: x+y), '-': (lambda x,y: x-y)}

def part1(acc, ip):
    if not instructions[ip]:
        return acc
    (cur, op, num) = re.match(r'([a-z]{3}) ([-+]{1})(\d+)', instructions[ip]).groups()
    instructions[ip] = ''
    if cur == 'acc':
        acc = ops[op] (acc, int(num))
        ip += 1
    elif cur == 'jmp':
        ip = ops[op] (ip, int(num))
    elif cur == 'nop':
        ip += 1
    return part1(acc, ip)

def exits(instructions, acc, ip, end):
    if ip == end:
        return acc
    elif ip > end or not instructions[ip]:
        return False
    (cur, op, num) = re.match(r'([a-z]{3}) ([-+]{1})(\d+)', instructions[ip]).groups()
    instructions[ip] = ''
    if cur == 'acc':
        acc = ops[op] (acc, int(num))
        ip += 1
    elif cur == 'jmp':
        ip = ops[op] (ip, int(num))
    elif cur == 'nop':
        ip += 1
    return exits(instructions, acc, ip, end)

def part2(end):
    for idx in range(end-1):
        new = instructions2.copy()
        ins = instructions2[idx].split()
        if ins[0] == 'jmp':
            new[idx] = 'nop ' + ins[1]
        elif ins[0] == 'nop':
            new[idx] = 'jmp ' + ins[1]
        exitVal = exits(new, 0, 0, end)
        if exitVal:
            return exitVal
    return False

print('Part 1:', part1(0,0))
print('Part 2:', part2(len(instructions2)))