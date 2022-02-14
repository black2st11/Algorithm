"""
https://www.acmicpc.net/problem/10773
"""

import sys

n = int(sys.stdin.readline().rstrip())

array = []

for _ in range(n):
    i = int(sys.stdin.readline().rstrip())

    if i == 0:
        array.pop()

    else:
        array.append(i)

print(sum(array))
