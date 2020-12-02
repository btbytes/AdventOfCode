#!/usr/bin/env python3
'''
Day 2, part a of the problem
'''

with open('02.txt') as f:
    lines = [l.strip() for l in f]

valids = 0
for line in lines:
    policy, password = line.split(': ')
    minmax, letter = policy.split(' ')
    mn, mx = minmax.split('-')
    mn, mx = int(mn), int(mx)
    count = len([x for x in password if x == letter])
    if mn <= count <= mx:
        valids += 1
print(valids)
