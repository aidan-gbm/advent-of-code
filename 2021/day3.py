in_file = 'day3.txt'
#in_file = 'day3test.txt'

# Read
data = [line.strip() for line in open(in_file)]

# Part 1
track = [0] * len(data[0])
for num, line in enumerate(data):
    for idx, bit in enumerate(line):
        track[idx] += int(bit)

gamma = epsilon = 0
for sig, bit in enumerate(track):
    gamma += (bit > (num + 1) / 2) << idx - sig
    epsilon += (bit < (num + 1) / 2) << idx - sig

print(f'Gamma: {gamma}, Epsilon: {epsilon}, Answer: {gamma * epsilon}')

# Part 1 Minified
data = [line.strip() for line in open(in_file)]
track = [sum(x) for x in zip(*[[int(bit) for bit in line] for line in data])]
g = sum([(bit > (num + 1) / 2) << len(data[0]) - sig - 1 for sig, bit in enumerate(track)])
e = sum([(bit < (num + 1) / 2) << len(data[0]) - sig - 1 for sig, bit in enumerate(track)])
print(f'Gamma: {g}, Epsilon: {e}, Answer: {g * e}')


