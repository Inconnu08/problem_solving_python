import operator


def hammingDistance(x, y):
    x = format(x, '04b')
    y = format(y, '04b')

    return abs(idx(x) - idx(y))


def idx(i):
    try:
        return i.index('1')
    except ValueError:
        return 0


def hamming2(str1, str2):
    str1 = format(str1, '04b')
    str2 = format(str2, '04b')
    assert len(str1) == len(str2)

    ne = operator.ne
    return sum(map(ne, str1, str2))


print(hammingDistance(1, 4))
print(hammingDistance(0, 1))
print(hammingDistance(93, 73))

print(hamming2(1, 4))
print(hamming2(0, 1))
print(hamming2(93, 73))
