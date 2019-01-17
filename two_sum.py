def two_sum(nums, target):

    for i, j in enumerate(nums):
        print(i)
        if target - j in nums and nums.index(target - j) != i:
            return i, nums.index(target - j)


print(two_sum([2, 11, 15, 7], 9))
