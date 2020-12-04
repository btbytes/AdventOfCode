#!/usr/bin/env python3
# Day 3, part B

from functools import reduce

def s(m, c, w, r, d):
    x = r
    t = 0
    i = 0
    for i in range(0, w - d, d):
        row = m[i]
        v = m[i+d][x]
        if v == '#':
            t += 1
        x += r
        x = x % c
    return t

if __name__ == '__main__':
    with open('03.txt') as f:
        m = [[c for c in r.strip()] for r in f]
    d = {1: 1, 3: 1, 5: 1, 7: 1, 1: 2}
    print(reduce(lambda x, y: x * y, [s(m,len(m[0]),len(m),k,v) for k,v in d.items()]))
