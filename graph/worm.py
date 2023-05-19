"""
https://www.acmicpc.net/problem/1012
"""

import sys

sys.setrecursionlimit(int(1e9))

t = int(sys.stdin.readline().rstrip())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, n, m):
    if y >= n or y < 0 or x < 0 or x >= m:
        return 0

    if graph[y][x] == 0:
        return 0

    graph[y][x] = 0
    for i in range(4):
        dfs(x + dx[i], y + dy[i], n, m)

    return 1


for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())

    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())

        graph[y][x] = 1

    result = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                result += dfs(x, y, n, m)

    print(result)
