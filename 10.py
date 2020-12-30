# 1. part
import re
inp = [int(i) for i in open('10.txt').read().splitlines()]

inp = '''16
10
15
5
1
11
7
19
6
12
4'''
inp = [int(i) for i in inp.splitlines()]

print(inp)
inp.sort()
print(inp)
nums = []

nums.append(inp[0])

for i in range(len(inp)):
    try:
        nums.append(inp[i+1]-inp[i])
    except:
        pass
nums.append(3)
print('Part 1:', nums.count(1) * nums.count(3))

result = []
for i in range(len(inp)):
    if i+
    for j in range(i + 1, len(inp)):
        for k in range(j + 1, len(inp)):
            print('hi')


