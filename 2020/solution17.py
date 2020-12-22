def readGrid(dimensions):
    grid = {}
    axis = [0] * dimensions
    with open('input/input17.txt') as f:
        for line in f:
            line = str(line.rstrip())
            for x, char in enumerate(line):
                axis[0] = x
                grid[tuple(axis)] = char
            axis[1] += 1
    return grid

def getNeighbors3D(cube):
    neighbors = []
    (tX, tY, tZ) = cube
    for x in range(tX-1,tX+2):
        for y in range(tY-1,tY+2):
            for z in range(tZ-1, tZ+2):
                neighbors.append((x,y,z))
    neighbors.remove(cube)
    return neighbors

def getNeighbors4D(cube):
    neighbors = []
    (tX, tY, tZ, tW) = cube
    for x in range(tX-1,tX+2):
        for y in range(tY-1,tY+2):
            for z in range(tZ-1,tZ+2):
                for w in range(tW-1,tW+2):
                    neighbors.append((x,y,z,w))
    neighbors.remove(cube)
    return neighbors

def cycle(grid):
    neighborGrid = {}
    for cube in grid:
        if grid[cube] == '#':
            if len(cube) == 3:
                neighbors = getNeighbors3D(cube)
            else:
                neighbors = getNeighbors4D(cube)
            for neighbor in neighbors:
                if neighbor in neighborGrid:
                    neighborGrid[neighbor] += 1
                else:
                    neighborGrid[neighbor] = 1
    
    active = 0
    newGrid = {}
    for cube in neighborGrid:
        if cube in grid:
            state = grid[cube]
        else:
            state = '.'

        count = neighborGrid[cube]
        if state == '#' and not (2 <= count <= 3):
            state = '.'
        elif state == '.' and count == 3:
            state = '#'
        
        newGrid[cube] = state
        if state == '#':
            active += 1

    return newGrid, active

def part1():
    grid = readGrid(3)
    for i in range(6):
        grid, count = cycle(grid)
    return count
    
def part2():
    grid = readGrid(4)
    for i in range(6):
        grid, count = cycle(grid)
    return count

print('Part 1:', part1())
print('Part 2:', part2())