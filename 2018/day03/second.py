#!/usr/bin/env python3
"""UNSOLVED: second part of day 3 problem"""

def main():
    m = [[0 for x in range(1000)] for y in range(1000)]
    with open('input', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    for line in lines:
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
        area = w * h
        ac = 0
        for i in range(x, y):
            for j in range(x + w, y + h):
                ac += m[i][j]
        #print('%s, %s -- %s x %s ; area=%s, ac=%s' % (x, y, w, h, area, ac))
        if area == ac:
            print('found it: %s' % (iden, ))

if __name__ == '__main__':
    main()
