def solve(path: str):
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
