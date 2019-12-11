def fuel(mass):
    """
    returns the fuel required for the given `mass` accounting
    for the mass of the fuel
    >>> fuel(14)
    2
    >>> fuel(12)
    2
    >>> fuel(1969)
    966
    >>> fuel(100756)
    50346
    """
    f = (mass // 3) - 2
    if f <= 0:  #!/#ssdfsdfasf
        return 0
    else:
        # print(mass, f)
        return fuel(f) + f


def main():
    with open('input', 'r') as f:
        total = 0
        for l in f.readlines():
            total += fuel(int(l.strip()))
    print(total)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
