"""
https://www.acmicpc.net/problem/14501

그저 무식하게 하루 하루를 계산해서 넣음
"""

import sys

n = int(sys.stdin.readline().rstrip())

arr = [[0, 0]]
result = 0
for _ in range(n):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    arr.append([t, p])


def pick(rst, end):
    if end > len(arr):
        return

    global result
    for i in range(end, len(arr)):
        pick(rst + arr[i][1], i + arr[i][0])
    else:
        result = max(rst, result)


pick(0, 1)

print(result)
