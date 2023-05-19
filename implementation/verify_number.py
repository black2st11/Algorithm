"""
https://www.acmicpc.net/problem/2475
"""

import sys

array = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0

for i in array:
    result += i ** 2

print(result % 10)
