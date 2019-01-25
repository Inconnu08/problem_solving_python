def hammingDistance(x, y):
    x = format(x, '04b')
    y = format(y, '04b')

    return abs(idx(x) - idx(y))


def idx(i):
    try:
        return i.index('1')
    except ValueError:
        return 0


print(hammingDistance(1, 4))
print(hammingDistance(0, 1))
print(hammingDistance(93, 73))
