"""
https://www.acmicpc.net/problem/11004
"""

import sys

t, k = map(int, sys.stdin.readline().rstrip().split())


array = list(map(int, sys.stdin.readline().rstrip().split()))


array.sort(key=lambda x: x)

print(array[k - 1])
