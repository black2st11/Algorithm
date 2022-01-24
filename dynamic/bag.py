"""
백준 12865
"""
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

things = [[0, 0]]


for _ in range(n):
    thing = list(map(int, sys.stdin.readline().rstrip().split()))
    things.append(thing)

dp = [[0] * (k + 1) for _ in range(n + 1)]

# 해당 부분은 [[0] * (k + 1)] 배열을 얕은복사로 복제함
# 그런데 안에 있는 [0]은 왜 얕은복사가 아닌지는 궁금함
# dp = [[0] * (k + 1) ] * (n + 1)


for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = things[i][0]
        value = things[i][1]
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])
print(dp)
print(dp[n][k])
