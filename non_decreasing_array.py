def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    truth = []

    for i, n in enumerate(nums):
        print(i, n)
        try:
            if n <= n[i]:
                truth.append(False)
            else:
                truth.append(True)
        except IndexError:
            pass

    print(truth)


checkPossibility([4, 2, 3])
checkPossibility([4, 2, 1])
