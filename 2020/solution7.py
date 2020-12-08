import re

with open('input7.txt') as f:
    rules = f.read()

class Bag:
    def __init__(self, name, bags):
        self.name = name
        self.bags = bags

def hasBag(name, bag):
    if bag.name == name:
        return True
    else:
        return any(hasBag(name, x) for x, y in bag.bags.items())

def numBags(bigBag):
    total = 1
    for bag, count in bigBag.bags.items():
        print(bag.name, count)
        total += int(count) * numBags(bag)
    return total

rule = re.compile(r"([a-z]+ [a-z]+) bags contain (.+)")
content = re.compile(r"(\d+) ([a-z]+ [a-z]+) bag")
bags = { bag: Bag(bag, contents) for bag, contents in rule.findall(rules) }
for bag in bags.values():
    bag.bags = {bags[inner]: n for n, inner in content.findall(bag.bags)}

# Part 1
count = 0
for name, bag in bags.items():
    if name == 'shiny gold':
        continue
    if hasBag('shiny gold', bag):
        count += 1
print('Part 1:', count)

# Part 2
print('Part 2:', numBags(bags['shiny gold'])-1)