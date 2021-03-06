# Day 1 part b of the problem 
# do not repeat over the numbers already picked
# Output :
# answer : 203481432
# time   : 0.30s

import time
import sys

start = time.time()

with open('01.txt') as f:
    expenses = [int(l.strip()) for l in f]

for ii, i in enumerate(expenses):
    for jj, j in enumerate(expenses[ii:]):
        for k in expenses[ii+jj:]:
            if i + j + k == 2020:
                print(f'answer : {i * j * k}')
                print(f'time   : {(time.time() - start)*1000:.2f}ms')
                sys.exit(0)
