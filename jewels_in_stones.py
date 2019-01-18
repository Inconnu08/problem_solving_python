def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    k = set(J.lower())
    s = list(S.lower())
    c = 0

    for n in s:
        if n in k:
            c = c + 1

    return c


numJewelsInStones("aA", "aAAbbbb")
