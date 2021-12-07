# Read input
in_file = 'day3.txt'
with open(in_file) as fd:
    draws = [int(d) for d in fd.readline().split(',')]
    rows = fd.readlines()
    boards = [[[int(n) for n in r.split()] for r in rows[i+1:i+6]] for i in range(0, len(rows), 6)]

def bingo(draws, board):
    row = any([all([n in draws for n in row]) for row in board])
    col = any([all([board[c][r] in draws for c in range(5)]) for r in range(5)])
    return row or col

for d in range(5, len(draws)):
    for b in boards:
        if bingo(draws[:d], b):
            print(f'Winning number: {draws[d-1]}')
            unmarked = sum([sum([n for n in r if n not in draws[:d]]) for r in b])
            print(f'Answer: {unmarked*draws[d-1]}')
            exit(0)

