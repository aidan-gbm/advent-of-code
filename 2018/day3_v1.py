import re

covered = set()
overlaps = set()
data = open('day3.txt', 'r')
claims = map(lambda line: map(int, re.findall(r'-?\d+', line)), data)
for (claim_num, x, y, w, h) in claims:
  for i in range(x, x+w):
    for j in range(y, y+h):
      if (i,j) in covered:
        overlaps.add((i,j))
      else:
        covered.add((i,j))

print(len(overlaps))