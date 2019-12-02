dataStream = open("day2-input.txt")
dataList = [int(x) for x in dataStream.readline().split(',')]

## Part 1
data = dataList.copy()
data[1] = 12
data[2] = 2

def opcode(ip, data):
  oc = data[ip]
  if (oc == 99):
    return data[0]
  else:
    arg1 = data[ip+1]
    arg2 = data[ip+2]
    res = data[ip+3]

    if (oc == 1):
      data[res] = data[arg1] + data[arg2]
    elif (oc == 2):
      data[res] = data[arg1] * data[arg2]
    else:
      print('Unexpected opcode {} at location {}!'.format(data[ip], ip))
      return -1

    return opcode(ip+4, data)

print('Part 1: ' + str(opcode(0, data)))

## Part 2

def validate(noun, verb):
  data = dataList.copy()
  data[1] = noun
  data[2] = verb

  if (opcode(0, data) == 19690720):
    return True
  else:
    return False

ans = None
for n in range(100):
  for v in range(100):
    if (validate(n,v)):
      ans = 100 * n + v

if ans:
  print('Part 2: ' + str(ans))
else:
  print('Part 2: Not found.')