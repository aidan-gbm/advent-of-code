from sys import argv

def day3_mcb(nums, idx):
    return int(sum([int(num[idx]) for num in nums]) >= (len(nums) / 2))

def day3_1(in_file):
    data = [line.strip() for line in open(in_file)]
    track = [sum(x) for x in zip(*[[int(bit) for bit in line] for line in data])]
    g = sum([(bit > (len(data) + 1) / 2) << len(data[0]) - sig - 1 for sig, bit in enumerate(track)])
    e = sum([(bit < (len(data) + 1) / 2) << len(data[0]) - sig - 1 for sig, bit in enumerate(track)])
    print(f'Gamma: {g}, Epsilon: {e}, Answer: {g * e}')

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
    print(oxy, co2, oxy * co2)

if __name__ == '__main__':
    if len(argv) == 3:
        func = f'day{argv[1]}_{argv[2]}'
        if func in locals():
            locals()[func](f'day{argv[1]}.txt')
        else:
            print('That problem hasn\'t been completed yet!')
    else:
        print(f'Usage: {argv[0]} <day #> <part #>')

