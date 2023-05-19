"""
백준 11055
"""

import sys

n = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().rstrip().split()))

dp = array[:]

for i in range(len(array)):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))
