"""
백준 2579
"""

import sys

n = int(sys.stdin.readline().rstrip())

stair = []
stair.append(0)
dp = [0] * (n + 1)

for i in range(n):
    stair.append(int(sys.stdin.readline().rstrip()))
stair.append(0)

if n == 1:
    print(stair[n])
else:

    dp[1] = stair[1]
    dp[2] = stair[2] + stair[1]

    for i in range(3, n + 1):
        dp[i] = stair[i] + max(dp[i - 2], stair[i - 1] + dp[i - 3])

    print(dp[n])
