import csv
import collections

f = open('day2.csv')
reader = csv.reader(f)

two = 0
three = 0
for line in reader:
  freqs = collections.Counter(line[0])
  gotTwo = False
  gotThree = False
  for ch, freq in freqs.items():
    if not gotTwo and int(freq) == 2:
      two += 1
      gotTwo = True
    if not gotThree and int(freq) == 3:
      three += 1
      gotThree = True

print(str(two * three))