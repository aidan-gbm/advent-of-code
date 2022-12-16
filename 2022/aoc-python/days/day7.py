from collections import defaultdict
from itertools import accumulate


def solve(path: str):
    with open(path) as fd:
        term = fd.readlines()

    sizes = defaultdict(int)
    for line in map(str.strip, term):
        if line[0] == '$':
            cmd, *arg = line.split()[1:]
            if cmd == 'cd':
                if arg[0] == '/':
                    cwd = ['/']
                elif arg[0] == '..':
                    cwd.pop()
                else:
                    cwd.append(arg[0])
        else:
            [size, _] = line.split()
            if size.isdigit():
                for d in accumulate(cwd):
                    sizes[d] += int(size)

    needed = sizes['/'] - 40000000
    to_del = next(filter(lambda s: s >= needed, sorted(sizes.values())))

    print('[+] Part 1:', sum(filter(lambda s: s <= 100000, sizes.values())))
    print('[+] Part 2:', to_del)
