def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    l = []

    for x in A:
        if x % 2 == 0:
            l.append(x)
        else:
            l = [x] + l

    return l


print(sortArrayByParity([2, 3, 6, 8, 9]))
