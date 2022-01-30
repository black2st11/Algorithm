"""
leet code : Maximum Difference Between Increasing Elements
"""


def maximum_difference(nums: list):
    result = -1
    temp = nums[0]

    for num in nums:
        if num - temp > 0:
            result = max(result, num - temp)
        else:
            temp = num
    return result


print(maximum_difference([1, 5, 2, 10]))
