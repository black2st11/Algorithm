"""
https://www.acmicpc.net/problem/11576
"""

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

m = int(sys.stdin.readline().rstrip())

prev = list(map(int, sys.stdin.readline().rstrip().split()))


mid = 0
prev = prev[::-1]

for i in range(len(prev)):
    mid += prev[i] * a ** i
result = []
while mid:
    remain = mid % b
    result.append(remain)
    mid = mid // b

result = result[::-1]

for i in result:
    print(i, end=" ")
