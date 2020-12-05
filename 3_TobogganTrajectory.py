# 1. part
inp = [i for i in open('3.txt').read().splitlines()]

# inp = '''..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#'''.splitlines()

tree = '#'
trees = 0

curr_pos = [0, 0]
slope = [3, 1]
i = 0

for i in range(len(inp)):
    inp[i] = inp[i]*100

i = 0
while i < len(inp) - 1:
    curr_pos = [curr_pos[0] + slope[0], curr_pos[1] + slope[1]]
    if inp[curr_pos[1]][curr_pos[0]] == tree:
        trees += 1
    i += slope[1]

print('Part 1:', trees)

# 2. part
inp = [i for i in open('3.txt').read().splitlines()]
tree = '#'
trees = 0

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
i = 0
result = 1

for i in range(len(inp)):
    inp[i] = inp[i]*1000

for slope in slopes:
    i = 0
    trees = 0
    curr_pos = [0, 0]
    while i < len(inp) - 1:
        curr_pos = [curr_pos[0] + slope[0], curr_pos[1] + slope[1]]
        if inp[curr_pos[1]][curr_pos[0]] == tree:
            trees += 1
        i += slope[1]

    # print(trees)
    result *= trees

print('Part 2:', result)


#better solution
inp = [i for i in open('3.txt').read().splitlines()]
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
i = 0
result = 1
G = []

ans = 1
for (dc, dr) in slopes:
    r = 0
    c = 0
    score = 0
    while r < len(G):
        c += dc
        r += dr
        if r < len(G) and G[r][c%len(G[r])] == '#':
            score += 1
    ans *= score
    if dc == 3 and dr == 1:
        print(score)

print(ans)
