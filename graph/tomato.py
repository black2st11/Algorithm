"""
https://www.acmicpc.net/problem/7576
"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, -0, 1]
graph = []
for _ in range(m):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))


def bfs():
    que = deque()
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                que.append((i, j, 0))
    while que:
        y, x, hour = que.popleft()

        for i in range(4):
            if y + dy[i] >= m or y + dy[i] < 0 or x + dx[i] >= n or x + dx[i] < 0:
                continue
            next_y = y + dy[i]
            next_x = x + dx[i]
            if graph[next_y][next_x] == 0:
                graph[next_y][next_x] = 1
                que.append((next_y, next_x, hour + 1))

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                print(-1)
                return

    print(hour)


bfs()
