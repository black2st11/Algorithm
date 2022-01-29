"""
leet code : Remove Duplicates from Sorted Array
"""


def remove_duplicates(nums: list):
    array = []
    empty_array = []
    nums.sort()

    for num in nums:
        if not num in array:
            array.append(num)
        else:
            empty_array.append("_")

    return array + empty_array


print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
