# Day 1 - part b of the problem
# Brute force solution

# Output :
# answer : 203481432
# ops    : 12929356
# time   : 4.28s

import sys
import time

start = time.time()
ops = 0

with open('01.txt') as f:
	expenses = [l.strip() for l in f]

for i in expenses:
	for j in expenses:
		for k in expenses:
			ops += 3
			if int(i)+int(j)+int(k) == 2020:
				print(f'answer : {int(i) * int(j) * int(k)}')
				print(f'ops    : {ops+1}')
				print(f'time   : %.2fs' % (time.time() - start, ) )
				sys.exit(0)
