"""
https://www.acmicpc.net/problem/15651
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

array = [1, 2, 3, 4, 5, 6, 7, 8]

is_pick = [False] * 8


def sequence(picked: list):
    if len(picked) >= m:
        print(" ".join(picked))
        return

    for i in range(n):
        picked.append(str(array[i]))
        sequence(picked)
        picked.pop()


sequence([])
