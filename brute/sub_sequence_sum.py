"""
https://www.acmicpc.net/problem/1182
"""

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0

picked = []


def pick(rst, idx):
    global cnt
    if sum(picked) == m and picked:
        cnt += 1

    if idx == n:
        return

    for i in range(idx, len(arr)):
        picked.append(arr[i])
        pick(picked, i + 1)
        picked.pop()


pick(0, 0)

print(cnt)
