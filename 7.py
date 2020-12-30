# 1. part
import re, copy
inp = [i for i in open('7.txt').read().splitlines()]

print(inp)
d = {}
gold_count = 0

# a = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.'''
# inp = a.splitlines()

reg = re.compile(r'\d')

for i in inp:
    if reg.search(i):
        m = i.split('contain ')
        newlist = m[1].split(', ')
        for j in range(len(newlist)):
            key = ' '.join(newlist[j].split()[1:3])
            print(key)
            if key in d.keys():
                d[key].add(' '.join(m[0].split()[:2]))
            else:
                d[key] = set()
                d[key].add(' '.join(m[0].split()[:2]))

print(d)

shiny_list = set()
looked = set()
before = 0
after = 34112321312

for i in d['shiny gold']:
    shiny_list.add(i)
    test_list = copy.deepcopy(shiny_list)
    while before != after:
        # test_list = set()
        before = len(test_list)
        for j in shiny_list:
            try:
                for a in list(d[j]):
                    test_list.add(a)
            except:
                pass
        for e in list(test_list):
            shiny_list.add(e)
        after = len(test_list)

print(len(shiny_list))
print(shiny_list)
