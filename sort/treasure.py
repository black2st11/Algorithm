"""
https://www.acmicpc.net/problem/1026
"""

import sys

n = int(sys.stdin.readline().rstrip())

a = list(map(int, sys.stdin.readline().rstrip().split()))

b = list(map(int, sys.stdin.readline().rstrip().split()))


array = sorted(b)

a.sort(reverse=True)
result = 0
for i in range(len(a)):
    result += a[i] * array[i]

print(result)
