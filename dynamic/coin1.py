"""
https://www.acmicpc.net/problem/2293
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

dp = [0] * (m + 1)

# 동전하나로 구하는 경우
# dp[j -i] == 0 일 때는 1이다
dp[0] = 1

for i in arr:
    for j in range(1, m + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[-1])
