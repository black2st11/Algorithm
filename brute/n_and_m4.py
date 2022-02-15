"""
https://www.acmicpc.net/problem/15652
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

array = [1, 2, 3, 4, 5, 6, 7, 8]

is_pick = [False] * 8


def sequence(picked: list, end):
    if len(picked) >= m:
        print(" ".join(picked))
        return

    for i in range(n):
        if array[i] >= end:
            picked.append(str(array[i]))
            sequence(picked, array[i])
            picked.pop()


sequence([], 0)
