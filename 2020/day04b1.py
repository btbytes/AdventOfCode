#!/usr/bin/env python
# Day 4, Part B
with open('04.txt') as f:
	passports = [b.replace('\n', ' ') for b in f.read().split('\n\n')]

def vr(yr, start, end):
	return yr.isnumeric() and start <= int(yr) <= end
	

def valid_hgt(hgt):
	units = hgt[-2:].lower()
	ht = hgt[:-2]
	if units in ['cm', 'in'] and ht.isnumeric():
		return {
			'cm': 150 <= int(ht) <= 193,
			'in': 59 <= int(ht) <= 76
		}[units]
	return False

reqd = set('ecl pid eyr hcl byr iyr cid hgt'.split(' '))
valids = 0
for l in passports:
	parts = l.strip().split(' ')
	r = {}
	for part in parts:
		k, v = part.split(':')
		r[k] = v
	if reqd.difference(set(r.keys())) in [set([]), set(['cid'])] \
		and vr(r['byr'], 1920, 2002) \
		and vr(r['iyr'], 2010, 2020) \
		and vr(r['eyr'], 2020, 2030) \
		and valid_hgt(r['hgt']) \
		and r['hcl'][0] == '#' and all([c in '0123456789abcdef' for c in r['hcl'][1:]]) \
		and r['ecl'].lower() in 'amb blu brn gry grn hzl oth'.split(' ') \
		and len(r['pid']) == 9 and r['pid'].isnumeric():
		valids += 1
print(valids)
