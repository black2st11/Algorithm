"""
leetcode : two_sum
"""


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


array = [2, 7, 11, 15]
tar = 9


print(two_sum(array, tar))
