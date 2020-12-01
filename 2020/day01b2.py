# Day 1 part b of the problem 
# do not repeat over the numbers already picked
# Output :
# answer : 203481432
# time   : 1.22s

import sys
import time

start = time.time()

with open('01.txt') as f:
  expenses = [l.strip() for l in f]

for ii, i in enumerate(expenses):
  for jj, j in enumerate(expenses[ii:]):
    for kk, k in enumerate(expenses[ii+jj:]):
      if int(i)+int(j)+int(k) == 2020:
        print(f'answer : {int(i) * int(j) * int(k)}')
        print(f'time   : %.2fs' % (time.time() - start, ) )
        sys.exit(0)
