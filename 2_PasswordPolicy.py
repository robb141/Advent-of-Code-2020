#part one
inp = [i for i in open('2.txt').read().splitlines()]
valid = 0
for i in inp:
    k = i.split(' ')
    if (k[2].count(k[1].replace(':', '')) <= int(k[0].split('-')[1])) and \
            (k[2].count(k[1].replace(':', '')) >= int(k[0].split('-')[0])):
        valid += 1
print(valid)


#part two
inp = [i for i in open('2.txt').read().splitlines()]
valid = 0
for i in inp:
    k = i.split(' ')
    k1 = k[1].replace(':', '')
    k0first = int(k[0].split('-')[0]) - 1
    k0second = int(k[0].split('-')[1]) - 1
    if (k1 in k[2][k0first] and k1 not in k[2][k0second]) or (k1 not in k[2][k0first] and k1 in k[2][k0second]):
        valid += 1
print(valid)

