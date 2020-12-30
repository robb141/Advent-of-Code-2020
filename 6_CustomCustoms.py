# 1. part
with open('6.txt', 'r') as f:
    inp = f.read()
    inp = inp.split('\n\n')

print(inp)
ans = []

for i in inp:
    yes_ans = []
    for k in i:
        if k != '\n' and k not in yes_ans:
            yes_ans.append(k)
    ans.append(len(yes_ans))

print('Part 1:', sum(ans))

ans2 = []
for i in inp:
    yes_ans = []
    i = i.split('\n')
    flag = True
    for k in i:
        if k == '':
            continue
        if flag:
            for j in k:
                if j not in yes_ans:
                    yes_ans.append(j)
            flag = False
        if not flag:
            for j in yes_ans[::-1]:
                if j not in k:
                    yes_ans.remove(j)
    ans2.append(len(yes_ans))

print(ans2)
print('Part 2:', sum(ans2))

