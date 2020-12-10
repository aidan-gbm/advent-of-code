from queue import PriorityQueue

def part1():
    q = PriorityQueue()
    with open('input10.txt') as f:
        maxVal = 0
        for line in f.readlines():
            last = int(line)
            q.put(last)
            maxVal = max(maxVal, last)
        q.put(maxVal+3)
    ones, threes, last = (0, 0, 0)
    while not q.empty():
        item = q.get()
        if item - last == 1:
            ones += 1
        elif item - last == 3:
            threes += 1
        last = item
    return ones * threes

def hasMultiple(num0, num2):
    return num2 - num0 <= 3

def numPaths(nums, goal):
    if nums[0] == goal:
        return 1
    options = 1
    if len(nums) > 2 and nums[2]-nums[0] <= 3:
        options += 1
    if len(nums) > 3 and nums[3]-nums[0] <= 3:
        options += 1
    if options == 1:
        return numPaths(nums[1:], goal)
    elif options == 2:
        return numPaths(nums[1:], goal) + numPaths(nums[2:], goal)
    else:
        return numPaths(nums[1:], goal) + numPaths(nums[2:], goal) + numPaths(nums[3:], goal)

def mult(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] * mult(nums[1:])

def part2():
    chargers = [0]
    with open('input10.txt') as f:
        chargers.extend(sorted(map(int, f.readlines())))
    chargers.append(chargers[-1] + 3)
    
    subs = []
    last = ()
    for idx in range(len(chargers)):
        if idx+2 < len(chargers) and hasMultiple(chargers[idx], chargers[idx+2]):
            if len(last) != 0:
                last = (last[0], idx+2)
            else:
                last = (idx,idx+2)
        elif len(last) != 0:
            subs.append(last)
            last = ()
    
    splits = []
    for sub in subs:
        splits.append(numPaths(chargers[sub[0]:sub[1]+1], chargers[sub[1]]))
    return mult(splits)

print('Part 1:', part1())
print('Part 2:', part2())