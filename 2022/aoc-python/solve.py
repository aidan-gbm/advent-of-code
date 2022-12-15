import argparse


def day_5(path: str):
    from copy import deepcopy

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


def day_4(path: str):
    with open(path) as fd:
        pairs = map(lambda s: s.strip().split(','), fd.readlines())

    full = partial = 0
    gen = (range(int(s[0]), int(s[1]) + 1) for p in pairs for s in map(lambda s: s.split('-'), p))
    for r1 in gen:
        r2 = next(gen)
        if all(n in r2 for n in r1) or all(n in r1 for n in r2):
            full += 1
            partial += 1
        elif any(n in r2 for n in r1) or any(n in r1 for n in r2):
            partial += 1

    print('[+] Part 1:', full)
    print('[+] Part 2:', partial)


def err(_):
    print('[-] That day\'s solution has not been implemented.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('day', type=int)
    parser.add_argument('--test', action='store_true')
    parser.set_defaults(test=False)
    args = parser.parse_args()

    func = f'day_{args.day}'
    input_file = f'test{args.day}.txt' if args.test else f'input{args.day}.txt'
    print(f'[#] Computing day {args.day}, test: {args.test}...')
    globals().get(func, err)('./input/' + input_file)
