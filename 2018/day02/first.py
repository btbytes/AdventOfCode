#!/usr/bin/env python3

import string


def main():
    with open('input', 'r') as f:
        twos = threes = count = 0
        for l in f.readlines():
            l = l.strip()
            s = ''.join(sorted(l))
            count += 1
            letters = string.ascii_lowercase
            counts = [l.count(letter) for letter in letters]
            print('%s -- %s -- %d -- %d' % (l, s, counts.count(2),
                                            counts.count(3)))

            two = counts.count(2)
            three = counts.count(3)
            if two > 1:
                two = 1
            if three > 1:
                three = 1
            twos += two
            threes += three

        print('count: %s' % (count, ))
        print('twos: %s, threes: %s. Checksum=%s' % (twos, threes,
                                                     twos * threes))


if __name__ == '__main__':
    main()
