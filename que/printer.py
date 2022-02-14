"""
https://www.acmicpc.net/problem/1966
"""

import sys

from collections import deque

t = int(sys.stdin.readline().rstrip())


def check_number(array, m, n):
    cnt = 1
    idx = m
    while array:
        if array[0] == max(array):
            array.popleft()
            if idx == 0:
                return cnt
            else:
                cnt += 1
                idx -= 1
        else:
            array.rotate(-1)
            if idx == 0:
                idx = len(array) - 1
            else:
                idx -= 1
    return n


for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())

    array = deque(map(int, sys.stdin.readline().rstrip().split()))
    if n == 1:
        print(1)
        continue

    print(check_number(array, m, n))
