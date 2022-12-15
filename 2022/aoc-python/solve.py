import argparse

input_dir = './input/'

def day_4(test: bool):
    input_file = 'test4.txt' if test else 'input4.txt'
    with open(input_dir + input_file) as fd:
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
    print(f'[#] Computing day {args.day}, test: {args.test}...')
    globals().get(func, err)(args.test)
