import csv
import collections

f = open('day2.csv')
reader = csv.reader(f)

def numDiffs(first, second):
  diffs = 0
  for ch1, ch2 in zip(first, second):
    if ch1 != ch2:
      diffs += 1
  return diffs

str1 = ''
str2 = ''
strings = set()
for line in reader:
  for s in strings:
    if numDiffs(line[0], s) == 1:
      str1 = line[0]
      str2 = s
      break
  if str1:
    break
  strings.add(line[0])

print('First\t', str1)
print('Second\t', str2)