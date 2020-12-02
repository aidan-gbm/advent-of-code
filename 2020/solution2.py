def valid(line):
    [rule, pwd] = line.split(': ')
    [nums, char] = rule.split()
    [num1, num2] = list(map(int,nums.split('-')))
    count = 0
    for x in pwd:
        if x == char: count += 1
    return count >= num1 and count <= num2

def valid2(line):
    [rule, pwd] = line.split(':')
    [nums, char] = rule.split()
    [num1, num2] = list(map(int, nums.split('-')))
    return (pwd[num1] == char) ^ (pwd[num2] == char)

def main():
    with open('input2.txt') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        if valid2(line): count += 1
    return count

if __name__ == '__main__':
    print(main())