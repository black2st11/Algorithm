"""
백준 9461
"""

import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4, 101):
    dp[i] = dp[i - 3] + dp[i - 2]

for i in range(n):
    t = int(sys.stdin.readline().rstrip())

    print(dp[t])
