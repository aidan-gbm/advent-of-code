def solve(path: str):
    with open(path) as fd:
        a = [[int(t) for t in row.strip()] for row in fd.readlines()]
        b = list(zip(*a))
        c = list(zip(*reversed(a)))
        d = list(zip(*reversed(b)))

    w = len(a[0])
    h = len(b[0])
    grid = [[0 for _ in range(w)] for _ in range(h)]
    for o, forest in enumerate(x for x in [a, b, c, d]):
        for y, row in enumerate(forest):
            top = -1
            for x, tree in enumerate(row):
                match o:
                    case 0:
                        grid[y][x] |= (tree > top)
                    case 1:
                        grid[x][y] |= (tree > top)
                    case 2:
                        grid[h-x-1][y] |= (tree > top)
                    case 3:
                        grid[y][w-x-1] |= (tree > top)
                top = max(tree, top)

    print('[+] Part 1:', sum(map(sum, grid)))
