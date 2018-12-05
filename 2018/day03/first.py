#!/usr/bin/env python3
"""SOLVED: first part of day 3 problem"""

def main():
    m = [[0 for x in range(1000)] for y in range(1000)]
    with open('input', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    for line in lines:
        # #1 @ 829,837: 11x22
        iden, fp = line.split('@')
        fp = fp.strip()
        at, size = fp.split(':')
        at = at.strip()
        size = size.strip()
        x, y = at.split(',')
        x = int(x) - 1
        y = int(y) - 1
        w, h = size.split('x')
        w = int(w)
        h = int(h)
        # print('%s, %s -- %s x %s' % (x, y, w, h))
        for a in range(w):
            for b in range(h):
                m[x + a][y + b] += 1

    two_or_more = 0
    for i in range(1000):
        for j in range(1000):
            if m[i][j] >= 2:
                two_or_more += 1
    print("two or more = %s" % (two_or_more,))

if __name__ == '__main__':
    main()
