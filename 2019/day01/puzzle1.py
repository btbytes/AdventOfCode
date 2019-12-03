def fuel(mass):
    """returns the fuel required for the given `mass`
    >>> fuel(14)
    2
    >>> fuel(12)
    2
    >>> fuel(1969)
    654
    >>> fuel(100756)
    33583
    """
    return (mass // 3) - 2


def main():
    with open('input', 'r') as f:
        total = 0
        for l in f.readlines():
            total += fuel(int(l.strip()))
    print(total)


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()
