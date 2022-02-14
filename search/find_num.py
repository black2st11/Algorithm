"""
https://www.acmicpc.net/problem/1920
계수 정렬을 할려고 했는데 범위가 너무 크기에 이분
"""

import sys

n = int(sys.stdin.readline().rstrip())

array = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

n = int(sys.stdin.readline().rstrip())

compare = list(map(int, sys.stdin.readline().rstrip().split()))


def bin(l, r, comp):
    while l <= r:
        mid = (l + r) // 2

        if array[mid] < comp:
            l = mid + 1
        elif array[mid] == comp:
            print(1)
            return
        elif array[mid] > comp:
            r = mid - 1
    print(0)


for i in compare:
    bin(0, len(array) - 1, i)

