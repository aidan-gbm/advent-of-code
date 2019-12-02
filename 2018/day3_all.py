from collections import defaultdict
import re

overlaps = {}
covered = defaultdict(list)
data = open('day3.txt', 'r')
claims = map(lambda line: map(int, re.findall(r'-?\d+', line)), data)

for (claim_num, x, y, w, h) in claims:
  overlaps[claim_num] = set()
  for i in range(x, x+w):
    for j in range(y, y+h):
      if (i,j) in covered:
        for claim in covered[(i,j)]:
          overlaps[claim].add(claim_num)
          overlaps[claim_num].add(claim)
      covered[(i,j)].append(claim_num)

print('Part 1:', len([loc for loc in covered if len(covered[loc]) > 1]))
print('Part 2:', [claim for claim in overlaps if len(overlaps[claim]) == 0][0])