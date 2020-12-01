# Day 1 - part b of the problem
# Brute force solution
# Output :
# answer : 203481432
# time   : 1.14s

import sys
import time

start = time.time()

with open('01.txt') as f:
    expenses = [int(l.strip()) for l in f]

for i in expenses:
    for j in expenses:
        for k in expenses:
            if i + j + k == 2020:
                print(f'answer : {i * j * k}')
                print(f'time   : %.2fs' % (time.time() - start, ) )
                sys.exit(0)
