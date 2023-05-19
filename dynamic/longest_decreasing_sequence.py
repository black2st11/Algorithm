"""
백준 11722
"""

import sys

t = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1] * t

for i in range(len(array)):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
