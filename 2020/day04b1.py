#!/usr/bin/env python
# Day 4, Part B

passports = []
with open('04.txt') as f:
	c = 0
	nr = True
	for line in f:
		if line != '\n':
			if nr == True:
				passports.append(line.strip() + ' ')
			else:
				passports[c] += line.strip() + ' '
			nr = False
		else:
			c += 1
			nr = True


def valid_byr(byr):
	try:
		byr = int(byr)
		return 1920 <= byr <=2002
	except:
		return False

def valid_iyr(iyr):
	try:
		iyr = int(iyr)
		return 2010 <= iyr <=2020
	except:
		return False

def valid_eyr(eyr):
	try:
		eyr = int(eyr)
		return 2020 <= eyr <=2030
	except:
		return False

def valid_hgt(hgt):
	units = hgt[-2:].lower()
	if units not in ['cm', 'in']:
		return False
	ht = int(hgt[:-2])
	try:
		if units == 'cm':
			return 150 <= ht <= 193
		if units == 'in':
			return 59 <= ht <= 76
	except:
		return False

def valid_hcl(hcl):
	return hcl[0] == '#' and all([c in '0123456789abcdef' for c in hcl[1:]])

def valid_ecl(ecl):
	return ecl.lower() in 'amb blu brn gry grn hzl oth'.split(' ')

def valid_pid(pid):
	return len(pid) == 9 and all([p.isdigit() for p in pid])

reqd = set('ecl pid eyr hcl byr iyr cid hgt'.split(' '))
valids = 0
for l in passports:
	parts = l.strip().split(' ')
	r = {}
	for part in parts:
		k, v = part.split(':')
		r[k] = v
	if reqd.difference(set(r.keys())) in [set([]), set(['cid'])] \
		and valid_byr(r['byr']) and valid_iyr(r['iyr']) \
		and valid_eyr(r['eyr']) and valid_hgt(r['hgt']) \
		and valid_hcl(r['hcl']) and valid_ecl(r['ecl']) \
		and valid_pid(r['pid']):
		valids += 1
print(valids)
