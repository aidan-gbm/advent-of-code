import re

def part1():
    count = 0
    with open('input4.txt') as f:
        contents = f.read()

    passports = contents.split('\n\n')
    for p in passports:
        fields_needed = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
        fields = p.split()
        for f in fields:
            fname = f.split(':')[0]
            fdata = f.split(':')[1]
            if fname == 'byr':
                if int(fdata) <= 2002 and int(fdata) >= 1920:
                        fields_needed.remove(fname)
            elif fname == 'iyr':
                if int(fdata) <= 2020 and int(fdata) >= 2010:
                        fields_needed.remove(fname)
            elif fname == 'eyr':
                if int(fdata) <= 2030 and int(fdata) >= 2020:
                    fields_needed.remove(fname)
            elif fname == 'hgt':
                if re.match(r'^((1[5678][0-9]|19[0-3])cm|(59|6[0-9]|7[1-6])in)$', fdata):
                    fields_needed.remove(fname)
            elif fname == 'hcl':
                if re.match(r'^#[0-9a-f]{6}$', fdata):
                    fields_needed.remove(fname)
            elif fname == 'ecl':
                if fdata in ['amb','blu','brn','gry','grn','hzl','oth']:
                    fields_needed.remove(fname)
            elif fname == 'pid':
                if re.match(r'^\d{9}$', fdata):
                    fields_needed.remove(fname)

        if len(fields_needed) == 0:
            count += 1

    return count

if __name__ == '__main__':
    print(part1())