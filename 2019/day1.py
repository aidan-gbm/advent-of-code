## Part 1

fuel = 0
with open("day1-input.txt") as input:
  for line in input:
    num = int(line) // 3 - 2
    fuel += num

print('Part 1 fuel: ' + str(fuel))

## Part 2

fuel = 0
with open("day1-input.txt") as input:
  for line in input:
    num = int(line) // 3 - 2
    while num > 0:
      fuel += num
      num = num // 3 - 2

print('Part 2 fuel: ' + str(fuel))