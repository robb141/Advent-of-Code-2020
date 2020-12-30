# 1. part
from copy import deepcopy
inp = [i for i in open('12.txt').read().splitlines()]

# print(inp)

inp = '''F10
N3
F7
R90
F11'''.splitlines()

print(inp)

d = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270
}

direction = 'E'
coor = [0, 0]


def move(direction, points, coordinates):
    if direction == 'E':
        coordinates[1] += points
    elif direction == 'W':
        coordinates[1] -= points
    elif direction == 'N':
        coordinates[0] += points
    elif direction == 'S':
        coordinates[0] -= points
    else:
        print('error')
    return coordinates


for i in inp:
    ins = i[0]
    pnts = int(i[1:])
    if ins in ('N', 'S', 'E', 'W'):
        move(ins, pnts, coor)
    elif ins == 'F':
        move(direction, pnts, coor)
    elif ins == 'L':
        new_conf = d[direction] - pnts
        if new_conf < 0:
            new_conf = 360 - abs(new_conf)
        for key, value in d.items():
            if value == new_conf:
                direction = key
    elif ins == 'R':
        new_conf = d[direction] + pnts
        if new_conf >= 360:
            new_conf = abs(new_conf - 360)
        for key, value in d.items():
            if value == new_conf:
                direction = key

print('Part 1:', abs(coor[0]) + abs(coor[1]))


def new_waypoint(new_direction, points, coordinates, char_coordinates):
    if new_direction == 'E':
        coordinates[1] = abs(points)
        char_coordinates[1] = new_direction
    elif new_direction == 'W':
        coordinates[1] = 0 - points
        char_coordinates[1] = new_direction
    elif new_direction == 'N':
        coordinates[0] = abs(points)
        char_coordinates[0] = new_direction
    elif new_direction == 'S':
        coordinates[0] = 0 - points
        char_coordinates[0] = new_direction
    else:
        print('error:', coordinates)
    return coordinates, char_coordinates


def get_value(conf, d):
    for key, value in d.items():
        if value == conf:
            return key

# def new_waypoint(new_direction, points, coordinates):
#     if new_direction == 'E':
#         coordinates[1] = points
#     elif new_direction == 'W':
#         coordinates[1] = 0 - points
#     elif new_direction == 'N':
#         coordinates[0] = points
#     elif new_direction == 'S':
#         coordinates[0] = 0 - points
#     else:
#         print('error')
#     return coordinates

coor = [0, 0]
waypoint = [1, 10]
char_waypoint = ['N', 'E']
char_c = ['N', 'E']

for i in inp:
    ins = i[0]
    pnts = int(i[1:])
    tmp = [0, 0]
    if ins == 'E':
        waypoint[1] += pnts
    elif ins == 'W':
        waypoint[1] -= pnts
    elif ins == 'N':
        waypoint[0] += pnts
    elif ins == 'S':
        waypoint[0] -= pnts
    elif ins == 'F':
        coor[0] += (waypoint[0] * pnts)
        coor[1] += (waypoint[1] * pnts)
    elif ins == 'L':
        dir1 = char_waypoint[0]
        new_conf = d[dir1] - pnts
        if new_conf < 0:
            new_conf = 360 - abs(new_conf)
        dir1 = get_value(new_conf, d)
        # for key, value in d.items():
        #     if value == new_conf:
        #         dir1 = key
        tmp, char_c = new_waypoint(dir1, waypoint[0], tmp, char_waypoint)

        dir2 = char_waypoint[1]
        new_conf = d[dir2] - pnts
        if new_conf < 0:
            new_conf = 360 - abs(new_conf)
        # for key, value in d.items():
        #     if value == new_conf:
        #         dir2 = key
        dir2 = get_value(new_conf, d)
        tmp, char_c = new_waypoint(dir2, waypoint[1], tmp, char_waypoint)
        waypoint = deepcopy(tmp)
        char_waypoint = deepcopy(char_c)

    elif ins == 'R':
        dir1 = char_waypoint[0]
        new_conf = d[dir1] + pnts
        if new_conf >= 360:
            new_conf = abs(new_conf - 360)
        dir1 = get_value(new_conf, d)
        # for key, value in d.items():
        #     if value == new_conf:
        #         dir1 = key
        tmp, char_c = new_waypoint(dir1, waypoint[0], tmp, char_waypoint)

        dir2 = char_waypoint[1]
        new_conf = d[dir2] + pnts
        if new_conf >= 360:
            new_conf = abs(new_conf - 360)
        # for key, value in d.items():
        #     if value == new_conf:
        #         dir2 = key
        dir2 = get_value(new_conf, d)
        tmp, char_c = new_waypoint(dir2, waypoint[1], tmp, char_waypoint)

        # print(tmp)
        waypoint = deepcopy(tmp)
        char_waypoint = deepcopy(char_c)
    print(coor, waypoint)

print('Part 2:', abs(coor[0]) + abs(coor[1]))



