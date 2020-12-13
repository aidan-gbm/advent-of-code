with open('input12.txt') as f:
    instructions = f.readlines()

def part1():
    coords = {'x':0,'y':0,'d':0}
    for instruction in instructions:
        direction = instruction[0]
        dist = instruction[1:].strip()
        if direction == 'N':
            coords['y'] += int(dist)
        elif direction == 'S':
            coords['y'] -= int(dist)
        elif direction == 'E':
            coords['x'] += int(dist)
        elif direction == 'W':
            coords['x'] -= int(dist)
        elif direction == 'L':
            coords['d'] = (coords['d'] - (int(int(dist) / 90))) % 4
        elif direction == 'R':
            coords['d'] = (coords['d'] + (int(int(dist) / 90))) % 4
        else:
            if coords['d'] == 0:
                coords['x'] += int(dist)
            elif coords['d'] == 1:
                coords['y'] -= int(dist)
            elif coords['d'] == 2:
                coords['x'] -= int(dist)
            else:
                coords['y'] += int(dist)
    return abs(coords['x']) + abs(coords['y'])

def part2():
    waypoint = {'x':10,'y':1}
    coords = {'x':0,'y':0,'d':0}
    for instruction in instructions:
        direction = instruction[0]
        dist = instruction[1:].strip()
        if direction == 'N':
            waypoint['y'] += int(dist)
        elif direction == 'S':
            waypoint['y'] -= int(dist)
        elif direction == 'E':
            waypoint['x'] += int(dist)
        elif direction == 'W':
            waypoint['x'] -= int(dist)
        elif direction == 'L':
            for i in range(int(int(dist) / 90)):
                waypoint = {'x':-waypoint['y'],'y':waypoint['x']}
        elif direction == 'R':
            for i in range(int(int(dist) / 90)):
                waypoint = {'x':waypoint['y'],'y':-waypoint['x']}
        else:
            for i in range(int(dist)):
                coords['x'] += waypoint['x']
                coords['y'] += waypoint['y']
    return abs(coords['x']) + abs(coords['y'])

print('Part 1:', part1())
print('Part 2:', part2())