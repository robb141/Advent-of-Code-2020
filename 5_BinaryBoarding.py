# 1. part
inp = [i for i in open('5.txt').read().splitlines()]

print(inp)
ids = []

for k in inp:
    rlo = 0
    rhi = 127
    r = 128

    clo = 0
    chi = 7
    c = 8
    for i in k:
        if i == 'F':
            rhi -= r / 2
            r /= 2
        elif i == 'B':
            rlo += r / 2
            r /= 2
        elif i == 'L':
            chi -= c / 2
            c /= 2
        else:
            clo += c / 2
            c /= 2
    ids.append(rhi * 8 + chi)


print('Part 1:', max(ids))

ids.sort()
ids = [int(i) for i in ids]
start = min(ids)

while start < max(ids):
    if start not in ids:
        print('Part 2:', start)
        break
    start += 1

