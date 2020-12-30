inp = [i for i in open('13.txt').read().splitlines()]

# inp = '''939
# 7,13,x,x,59,x,31,19'''.splitlines()

my_time = int(inp[0])
print(inp)
print(my_time)
wait_time = 9999

times = [int(i) for i in inp[1].split(',') if i != 'x']
print(times)

for i in times:
    if (i - my_time % i) < wait_time:
        wait_time = i - my_time % i
        result = i * wait_time
        # print(wait_time)

print('Part 1:', result)


