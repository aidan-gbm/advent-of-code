import queue

def valid(preamble, num):
    for x in preamble:
        for y in preamble[1:]:
            if x != y and x + y == num:
                return True
    return False

def part1():
    preamble = []
    with open('input9.txt') as f:
        for i in range(25):
            preamble.append(int(f.readline()))
        nextVal = f.readline().strip()
        while nextVal:
            if valid(preamble, int(nextVal)):
                preamble.pop(0)
                preamble.append(int(nextVal))
                nextVal = f.readline().strip()
            else:
                return nextVal

def part2(target):
    nums = []
    with open('input9.txt') as f:
        xmasList = list(map(int, f.readlines()))
    while xmasList or nums:
        if sum(nums) > target:
            nums.pop(0) 
        elif xmasList:
            nums.append(xmasList.pop(0))
        if sum(nums) == target:
            return max(nums) + min(nums)

target = part1()
print('Part 1:', target)
print('Part 2:', part2(int(target)))