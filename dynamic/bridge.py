"""
https://www.acmicpc.net/problem/1010

y = 1 일 때는 x 만큼 증가

y == x 일 경우 1

y > x 보다 큰 경우는 성립이 불가

나머지의 경우는

[y][x] = [y-1][x-1] + [y][x-1] 
"""

import sys

arr = [[0] * 31 for _ in range(31)]

for i in range(len(arr)):
    arr[1][i] = i

for y in range(2, len(arr)):
    for x in range(1, len(arr)):
        if y > x:
            arr[y][x] = 0
        elif y == x:
            arr[y][x] = 1
        else:
            arr[y][x] = arr[y - 1][x - 1] + arr[y][x - 1]

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())

    print(arr[n][m])
