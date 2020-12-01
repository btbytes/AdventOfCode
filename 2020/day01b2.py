# Day 1 part b of the problem 
# do not repeat over the numbers already picked
# Output :
# answer : 203481432
# ops    : 3654046
# time   : 1.32s


import sys
import time

start = time.time()
ops = 0

with open('01.txt') as f:
  expenses = [l.strip() for l in f]

for ii, i in enumerate(expenses):
  for jj, j in enumerate(expenses[ii:]):
    for kk, k in enumerate(expenses[ii+jj:]):
      ops += 3
      if int(i)+int(j)+int(k) == 2020:
        print(f'answer : {int(i) * int(j) * int(k)}')
        print(f'ops    : {ops+1}')
        print(f'time   : %.2fs' % (time.time() - start, ) )
        sys.exit(0)
