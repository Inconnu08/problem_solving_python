def diStringMatch(S):
    """
    :type S: str
    :rtype: List[int]
    """
    lo, hi = 0, len(S)
    ans = []
    for x in S:
        if x == 'I':
            ans.append(lo)
            lo += 1
        else:
            ans.append(hi)
            hi -= 1

    return ans + [lo]


print(diStringMatch("IDID"))
print(diStringMatch("III"))
print(diStringMatch("DDI"))
