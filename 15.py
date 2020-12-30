inp = [0,1,5,10,3,12,19]
# inp = [0,3,6]

d = {}
last = 0
i = 0

for i in range(len(inp)):
    d[i+1] = inp[i]
    last = d[i+1]


print(d)
print(last)
i += 1
print(i)

while i < 30000000:
    if sum(x == last for x in d.values()) < 2:
        d[i+1] = 0
    else:
        a = [k for k, v in d.items() if v == last]
        if len(a) > 2:
            del d[a[0]]
        d[i+1] = a[-1] - a[-2]
    last = d[i + 1]
    i += 1

print(d[2020])
print(last)

