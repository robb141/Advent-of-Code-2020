# 1. part
from copy import deepcopy
inp = [i for i in open('11.txt').read().splitlines()]

# inp = '''L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# '''.splitlines()

print(inp)


def count_hash(grid):
    num_count = 0
    for i in range(len(grid)):
        num_count += grid[i].count('#')
    return num_count


def is_valid(row, column):
    if row < 0 or row >= len(inp) or column < 0 or column >= len(inp[row]):
        return False
    else:
        return True


before = count_hash(inp)
after = 0

# print(before)

while before != after or after == 0:
    new_list = deepcopy(inp)
    before = count_hash(new_list)
    for r in range(len(inp)):
        for c in range(len(inp[r])):
            hashes = 0
            if inp[r][c] == '.':
                continue

            if is_valid(r + 0, c + 1) and inp[r + 0][c + 1] == '#':
                hashes += 1
            if is_valid(r + 1, c + 0) and inp[r + 1][c + 0] == '#':
                hashes += 1
            if is_valid(r + 1, c + 1) and inp[r + 1][c + 1] == '#':
                hashes += 1
            if is_valid(r - 0, c - 1) and inp[r - 0][c - 1] == '#':
                hashes += 1
            if is_valid(r - 1, c - 0) and inp[r - 1][c - 0] == '#':
                hashes += 1
            if is_valid(r - 1, c - 1) and inp[r - 1][c - 1] == '#':
                hashes += 1
            if is_valid(r + 1, c - 1) and inp[r + 1][c - 1] == '#':
                hashes += 1
            if is_valid(r - 1, c + 1) and inp[r - 1][c + 1] == '#':
                hashes += 1

            if inp[r][c] == 'L' and hashes == 0:
                new_str = new_list[r][:c] + '#' + new_list[r][c+1:]
                new_list[r] = new_str
            elif inp[r][c] == '#' and hashes >= 4:
                new_str = new_list[r][:c] + 'L' + new_list[r][c+1:]
                new_list[r] = new_str
            else:
                pass
    after = count_hash(new_list)
    inp = deepcopy(new_list)

print('Part 1:', after)
