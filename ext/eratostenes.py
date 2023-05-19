"""
https://www.acmicpc.net/problem/2960
"""

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

array = [0] * (n + 1)

result = []
for i in range(2, n + 1):
    for j in range(1, n + 1):
        if i * j > n:
            break
        if array[i * j] == 0:
            result.append(i * j)
            array[i * j] = 1

print(result[m - 1])
