# 1. part
inp = [i for i in open('9.txt').read().splitlines()]

# inp = '''35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
# '''.splitlines()

inp = [int(i) for i in inp]
print(inp)
preamble = 25

lo = 0
hi = 0 + preamble

while True:
    flag = False
    for i in range(lo, hi):
        for j in range(i+1, hi):
            if inp[i] + inp[j] == inp[hi]:
                flag = True
    if not flag:
        weakness = inp[hi]
        print('Part 1:', weakness)
        break
    lo += 1
    hi += 1


# Part 2
lo = 0
for i in range(lo, hi):
    result = inp[i]
    j = i + 1
    while result <= weakness:
        if result + inp[j] == weakness:
            print('Part 2:', min(inp[i:j]) + max(inp[i:j]))
            exit()
        result += inp[j]
        j += 1

