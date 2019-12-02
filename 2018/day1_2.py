import csv
import itertools

f = open('day1.csv')
reader = csv.reader(f)

freq = 0
seen = { 0 }
for step in itertools.cycle(reader):
  freq += int(step[0])
  if freq in seen:
    print(freq)
    break
  seen.add(freq)