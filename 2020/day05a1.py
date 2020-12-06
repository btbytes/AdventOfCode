# Day 5, Part A
# from math import min, max

with open('05.txt') as f:
    passes = [l.strip() for l in f]

def seatid(bpass):
    """
    >>>seatid(FBFBBFFRLR)
    357
    """
    c = list(range(127))
    for b in bpass[:7]:
        x = len(c) // 2
        if b == 'F':
            c = c[:x]
        else:
            c = c[x:]
    k = min(c) + 1
    c = list(range(7))
    for b in bpass[7:]:
        x = len(c)//2
        if b == 'R':
            c = c[x:]
        else:
            c = c[:x]
    try:
        m = max(c) + 1
    except:
        m = 0
        print(bpass, k, c)
    return k * 8 + m


with open('05.txt') as f:
    passes = [l.strip() for l in f]
print(max([seatid(bp) for bp in passes]))