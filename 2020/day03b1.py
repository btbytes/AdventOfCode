#!/usr/bin/env python3
# Day 3, part B

def sloped(mat, ncols, nrows, r, d):
    x = r
    trees = 0
    i = 0
    for i in range(0, nrows - d, d):
        row = mat[i]
        v = mat[i+d][x]
        if v == '#':
            trees += 1
        x += r
        x = x % ncols
    return trees

if __name__ == '__main__':
    with open('03.txt') as f:
        mat = [[c for c in r.strip()] for r in f]
    ncols = len(mat[0])
    nrows = len(mat)
    a = sloped(mat=mat, ncols=ncols, nrows=nrows, r=1, d=1)
    b = sloped(mat=mat, ncols=ncols, nrows=nrows, r=3, d=1)
    c = sloped(mat=mat, ncols=ncols, nrows=nrows, r=5, d=1)
    d = sloped(mat=mat, ncols=ncols, nrows=nrows, r=7, d=1)
    e = sloped(mat=mat, ncols=ncols, nrows=nrows, r=1, d=2)
    print(f'answer = {a * b * c * d * e}')
