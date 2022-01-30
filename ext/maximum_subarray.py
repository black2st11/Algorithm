"""
leet code : Maximum Subarray

처음에는 음수가 최대합이 나올 줄 알고
완전 탐색으로 해서 진행을 했지만 시간 초과 발생

나중에 조건을 보니 결과 값은 무조건 양수여서
양수 밑으로 내려가는 값들은 답이 될 수 가 없기 때문에
-가 나오는 경우 0으로 초기화
"""


def max_subarray(nums: list):
    result = sum(nums)
    temp = 0
    for num in nums:
        temp += num

        if result < temp:
            result = temp

        if temp < 0:
            temp = 0
    return result


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
