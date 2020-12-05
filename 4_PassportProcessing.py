import re

with open('4.txt', 'r')  as f:
    inp = f.read()
    # print(inp)
    inp = inp.split('\n\n')
    inp = [i.replace('\n', ' ') for i in inp]
    # inp = {k: v for k, v in inp}
    print(inp)


d = {
    'byr':  re.compile(r'(19[2-9][0-9]|200[0-2])'),
    'iyr': re.compile(r'(201[0-9]|2020)'),
    'eyr': re.compile(r'(202[0-9]|2030)'),
    'hgt': re.compile(r'(^1[5-8][0-9]cm|^19[0-3]cm|^59in|^6[0-9]in|^7[0-6]in)'),
    'hcl': re.compile(r'^#([0-9]|[a-f]){6}'),
    'ecl': re.compile(r'(amb|blu|brn|gry|grn|hzl|oth)'),
    'pid': re.compile(r'^\d{9}$')
}

count_valid = 0
looked = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
num_count = 0

for i in inp:
    flag = False
    for j in looked:
        if j in i:
            pass
        elif j == 'cid':
            pass
        else:
            flag = True
    if not flag:
        num_count += 1
        splitted = i.split(' ')
        for k, v in d.items():
            for j in splitted:
                if k == j.split(':')[0]:
                    if not d[k].search(j.split(':')[1]):
                        flag = True
        if not flag:
            count_valid += 1


print('Part 1:', num_count)
print('Part 2:', count_valid)
