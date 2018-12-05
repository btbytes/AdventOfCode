#!/usr/bin/env python3


def diffcount(x, y):
    xa = list(x)
    ya = list(y)
    dc = 0
    common = []
    for i in range(len(xa)):
        if xa[i] != ya[i]:
            dc += 1
        else:
            common.append(xa[i])
    return (dc, ''.join(common))


def main():
    with open('input', 'r') as f:
        lines = [el.strip() for el in f.readlines()]
        for a in lines:
            for b in lines:
                dc = diffcount(a, b)
                if dc[0] == 1:
                    print('%s -- %s -- %d' % (a, b, dc[0]))
                    print(dc[1])


if __name__ == '__main__':
    main()
