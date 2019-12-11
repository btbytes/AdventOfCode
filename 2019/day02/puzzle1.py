def solve(nums):
    """
    >>> solve([1,0,0,0,99])
    [2, 0, 0, 0, 99]
    """
    p = 0  # position
    while p < len(nums):
        opcode = nums[p]
        if opcode == 99:
            return nums
        p1 = nums[p + 1]
        n1 = nums[p1]
        p2 = nums[p + 2]
        n2 = nums[p2]
        if opcode == 1:
            r = n1 + n2
        if opcode == 2:
            r = n1 * n2
        location = nums[p + 3]
        nums[location] = r
        p += 4
    return nums


def main():
    with open('input', 'r') as f:
        nums = [int(i) for i in f.readline().split(',')]
    nums[1] = 12
    nums[2] = 2
    print(solve(nums))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()