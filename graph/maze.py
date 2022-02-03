"""
https://www.acmicpc.net/problem/2178
"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, -0, 1]
graph = []
for _ in range(n):
    temp_list = []
    text = sys.stdin.readline().rstrip()
    for i in text:
        temp_list.append(int(i))
    graph.append(temp_list)


def bfs():
    que = deque()

    que.append((0, 0, 0))
    while que:
        y, x, hour = que.popleft()

        if y + 1 == n and x + 1 == m:
            return hour + 1

        for i in range(4):
            if y + dy[i] >= n or y + dy[i] < 0 or x + dx[i] >= m or x + dx[i] < 0:
                continue

            next_y = y + dy[i]
            next_x = x + dx[i]
            if graph[next_y][next_x] == 1:
                graph[next_y][next_x] = 0
                que.append((next_y, next_x, hour + 1))


print(bfs())
