from copy import deepcopy


def solve(path: str):
    with open(path) as fd:
        lines = fd.readlines()
        start = lines[:lines.index('\n')]
        steps = lines[lines.index('\n') + 1:]

    stacks = [[] for _ in range(len(start[-1]) // 4)]
    for line in start[:-1]:
        for idx in range(len(stacks)):
            if line[idx*4+1] != ' ':
                stacks[idx].append(line[idx*4+1])

    stacks1 = list(map(lambda s: list(reversed(s)), stacks))
    stacks2 = deepcopy(stacks1)
    for step in steps:
        _, num, _, src, _, dst = step.split()
        for _ in range(int(num)):
            stacks1[int(dst)-1].append(stacks1[int(src)-1].pop())

        stacks2[int(dst)-1].extend(stacks2[int(src)-1][-int(num):])
        stacks2[int(src)-1] = stacks2[int(src)-1][:-int(num)]

    print('[+] Part 1:', ''.join(s[-1] for s in stacks1))
    print('[+] Part 2:', ''.join(s[-1] for s in stacks2))
