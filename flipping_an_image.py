def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    ls = []
    for l in A:
        l.reverse()
        ls.append([1 if x == 0 else 0 for x in l])

    return ls


print(flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
