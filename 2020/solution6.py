with open('input6.txt') as f:
    groups = f.read().split('\n\n')

def part1():
    count = 0
    for group in groups:
        yes = set()
        for user in group.split('\n'):
            for ans in user:
                yes.add(ans)
        count += len(yes)
    return count

def part2():
    count = 0
    for group in groups:
        users = [u for u in group.split('\n') if u]
        allYes = users[0]
        for user in users[1:]:
            for ans in allYes:
                if ans not in user:
                    allYes = allYes.replace(ans,'')
        count += len(allYes)
    return count

print('Part 1:', part1())
print('Part 2:', part2())