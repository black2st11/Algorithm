"""
leet code : Search Insert Position
"""


def search_insert_position(nums: list, target: int):
    try:
        return nums.index(target)
    except:
        for i in range(len(nums)):
            if nums[i] > target:
                return i
        else:
            return len(nums)


print(search_insert_position([1, 3, 5, 6], 7))
