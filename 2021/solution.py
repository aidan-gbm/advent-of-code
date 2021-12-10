from sys import argv


def day1_1(in_file):
    data = [int(line) for line in open(in_file)]
    return sum([a > b for a, b in zip(data[1:], data)])

def day1_2(in_file):
    data = [int(line) for line in open(in_file)]
    windows = list(map(sum, zip(data, data[1:], data[2:])))
    return sum([a > b for a, b in zip(windows[1:], windows)])


def day2_1(in_file):
    data = [(a, int(b)) for a, b in [x.split() for x in open(in_file)]]
    pos = sum([b for a, b in data if a == 'forward'])
    depth = sum([-b if a == 'up' else b if a == 'down' else 0 for a, b in data])
    return pos * depth

def day2_2(in_file):
    data = [(a, int(b)) for a, b in [x.split() for x in open(in_file)]]
    aim = pos = dep = 0
    for d, n in data:
        aim = aim + n if d[0] == 'd' else aim - n if d[0] == 'u' else aim
        dep = dep + aim * n if d[0] == 'f' else dep
        pos = pos + n if d[0] == 'f' else pos
    return pos * dep


def day3_mcb(nums, idx):
    return int(sum([int(num[idx]) for num in nums]) >= (len(nums) / 2))

def day3_1(in_file):
    data = [line.strip() for line in open(in_file)]
    g = sum([b << i for i, b in enumerate([day3_mcb(data, j) for j in range(len(data[0]))][::-1])])
    e = sum([b << i for i, b in enumerate([int(not day3_mcb(data, j)) for j in range(len(data[0]))][::-1])])
    return g * e

def day3_2(in_file):
    oxy = [line.strip() for line in open(in_file)]
    co2 = oxy.copy()
    for idx in range(len(oxy[0])):
        if len(oxy) > 1:
            mcb = day3_mcb(oxy, idx)
            oxy = list(filter(lambda x: int(x[idx]) == mcb, oxy))
        if len(co2) > 1:
            lcb = int(not day3_mcb(co2, idx))
            co2 = list(filter(lambda x: int(x[idx]) == lcb, co2))
    oxy = sum([int(bit) << idx for idx, bit in enumerate(oxy[0][::-1])])
    co2 = sum([int(bit) << idx for idx, bit in enumerate(co2[0][::-1])])
    return oxy * co2


if __name__ == '__main__':
    if len(argv) == 3:
        func = f'day{argv[1]}_{argv[2]}'
        if func in locals():
            ans = locals()[func](f'day{argv[1]}.txt')
            print(f'Day {argv[1]}.{argv[2]}:', ans)
        else:
            print('That problem hasn\'t been completed yet!')
    else:
        print(f'Usage: {argv[0]} <day #> <part #>')

