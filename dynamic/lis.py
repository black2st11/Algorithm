"""
최장 부분 수열
"""

import sys

# 원소 갯수
n = int(sys.stdin.readline().rstrip())

# 배열 입력
array = list(map(int, sys.stdin.readline().rstrip().split()))

# 메모 값을 1로 초기화 기본적으로 부분수열의 최솟값은 본인 혼자일 경우인 1이기 때문에
dp = [1] * n

for i in range(len(array)):
    # 기본으로 1인 경우
    res = 1
    for j in range(i):
        # 현재 돌아가는 A[I] > A[J] 일 경우에는 비교 순간마다 D[I] = D[J] + 1 형식
        if array[i] > array[j]:
            res = max(res, dp[j] + 1)
    dp[i] = res
print(dp)

# 7
# 10 40 50 20 30 40 50
