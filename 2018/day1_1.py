import csv

f = open('day1.csv')
reader = csv.reader(f)

cur = 0
for step in reader:
  cur += int(step[0])

print(str(cur))