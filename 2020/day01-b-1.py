with open('01.txt') as f:
	expenses = [l.strip() for l in f]
expenses.sort()	

for i in expenses:
	for j in expenses:
		for k in expenses:
			if int(i)+int(j)+int(k) == 2020:
				print(int(i) * int(j) * int(k))
