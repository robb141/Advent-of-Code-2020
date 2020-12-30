# 1. part
from copy import deepcopy

inp = [i for i in open('8.txt').read().splitlines()]

print(inp)
acc = 0
flag = False
instructions = []

i = 0

while i not in instructions:
    instructions.append(i)
    in_name = inp[i].split()[0]
    if in_name == 'nop':
        i += 1
    elif in_name == 'acc':
        acc += int(inp[i].split()[1])
        i += 1
    elif in_name == 'jmp':
        i += int(inp[i].split()[1])


print('Part 1:', acc)

for k in range(len(inp)):
    if flag:
        break
    else:
        new_inp = deepcopy(inp)
        if new_inp[k].split()[0] == 'nop':
            new_inp[k] = 'jmp' + new_inp[k][3:]
        elif new_inp[k].split()[0] == 'jmp':
            new_inp[k] = 'nop' + new_inp[k][3:]
        else:
            continue
        acc = 0
        instructions = []
        i = 0
        while i not in instructions:
            instructions.append(i)
            in_name = new_inp[i].split()[0]
            if in_name == 'nop':
                i += 1
            elif in_name == 'acc':
                acc += int(new_inp[i].split()[1])
                i += 1
            elif in_name == 'jmp':
                i += int(new_inp[i].split()[1])
            if i == len(new_inp):
                flag = True
                break

print('Part 2:', acc)


# Jonathan Paulson solution:
def run(P, ip, acc):
    words = P[ip].split()
    if words[0] == 'acc':
        acc += int(words[1])
        ip += 1
    elif words[0] == 'nop':
        ip += 1
    elif words[0] == 'jmp':
        ip += int(words[1])
    return ip, acc


P = [i for i in open('8.txt').read().splitlines()]
ip = 0
acc = 0
seen = set()
while True:
    if ip in seen:
        print(acc)
        break
    seen.add(ip)
    ip, acc = run(P, ip, acc)

for change in range(len(P)):
    Pmod = deepcopy(P)
    if Pmod[change][0] == 'nop':
        Pmod[change][0] = 'jmp'
    elif Pmod[change][0] == 'jmp':
        Pmod[change][0] = 'nop'
    else:
        continue
    t = 0
    ip = 0
    acc = 0
    while 0 <= ip <= len(Pmod) and t < 1000:
        t += 1
        ip, acc = run(Pmod, ip, acc)
    if ip == len(Pmod):
        print(acc)

