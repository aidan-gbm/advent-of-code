import time

with open('input/input15.txt') as f:
    nums = list(map(int, f.readline().split(',')))

def count(n):
    counter = 1
    last = 0
    history = {}
    for num in nums:
        history[num] = (counter, False)
        counter += 1
        last = num

    while (counter <= n):
        oHist = history[last]
        if oHist[1]:
            last = oHist[0] - oHist[1]
        else:
            last = 0
        if last in history:
            history[last] = (counter, history[last][0])
        else:
            history[last] = (counter, False)
        counter += 1
    return last

print('Part 1:', count(2020))
start = time.time()
print('Part 2:', count(30000000))
print(time.time() - start)