# Day 5, Part B
# @btbytes

def seatid(bpass):
    def f(s, h, p, m):
        c = list(range(h))
        for b in s:
            x = len(c) // 2
            if b == p:
                c = c[:x]
            else:
                c = c[x:]
        k = 0 if (len(c) == 0) else m(c) + 1
        return k
    k = f(bpass[:7], 127, 'F', min)
    m = f(bpass[7:], 7, 'L', max)
    return k * 8 + m


with open('05.txt') as f:
    sids = [seatid(p) for p in [l.strip() for l in f]]
sids.sort()
for i in range(sids[0], sids[-1]):
    if i not in sids:
        print(i)

