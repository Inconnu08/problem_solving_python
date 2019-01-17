def two_sum_ii(numbers, target):
    index = {}
    for i, n in enumerate(numbers):
        c = target - n
        if c in index:
            return [index[c] + 1, i + 1]
        index[n] = i
    return []


print(two_sum_ii([2, 7, 11, 15], 9))
print(two_sum_ii([2, 11, 7, 15], 9))
print(two_sum_ii([-1, 0], -1))
