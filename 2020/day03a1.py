#!/usr/bin/env python3

# Day 3, part A

with open('03.txt') as f:
    mat = [[c for c in r.strip()] for r in f]
ncols = len(mat[0])

x = 3
trees = 0

for r, row in enumerate(mat[:-1]):
    v = mat[r+1][x]
    if v == '#':
        trees += 1
    x += 3
    x = x % ncols
print(trees)