#!/usr/bin/env python

# Day 4, Part A

with open('04.txt') as f:
	rraw = []
	c = 0
	nr = True
	for line in f:
		if line != '\n':
			if nr == True:
				rraw.append(line.strip() + ' ')
			else:
				rraw[c] += line.strip() + ' '
			nr = False
		else:
			c += 1
			nr = True

valids = 0
reqd = set('ecl pid eyr hcl byr iyr cid hgt'.split(' '))

for l in rraw:
	parts = l.strip().split(' ')
	r = {}
	for part in parts:
		k, v = part.split(':')
		r[k] = v
	if reqd.difference(set(r.keys())) in [set([]), set(['cid'])]:
		valids += 1
print(valids)

