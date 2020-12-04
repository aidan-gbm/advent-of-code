def travel(right, down):
    hits = 0
    posX = 0
    with open('input3.txt') as f:
        line = f.readline().rstrip()
        while line:
            if line[posX % len(line)] == '#': hits += 1
            posX += right
            for x in range(down):
                line = f.readline().rstrip()
    return hits

res = travel(1,1) * travel(3,1) * travel(5,1) * travel(7,1) * travel (1,2)
print(res)