"""
https://www.acmicpc.net/problem/2146
"""
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

graph = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))


def bfs(row, col):
    if graph[row][col] == 0 or graph[row][col] == 2:
        return []

    que = deque()
    que.append((row, col))

    edge = set()
    while que:
        row, col = que.popleft()
        graph[row][col] = 2

        for i in range(4):
            next_x, next_y = col + dx[i], row + dy[i]

            if next_x >= n or next_x < 0 or next_y >= n or next_y < 0:
                continue

            if graph[next_y][next_x] == 0:
                edge.add((row, col))
            elif graph[next_y][next_x] == 1:
                que.append((next_y, next_x))
            else:
                pass

    return list(edge)


island = []

for i in range(n):
    for j in range(n):
        temp = bfs(i, j)
        if len(temp) > 0:
            island.append(temp)

result = int(1e9)

for i in range(len(island)):
    for j in range(1, len(island)):
        for left in island[i]:
            for right in island[j]:
                if abs(left[0] - right[0]) + abs(left[1] - right[1]) == 0:
                    continue
                result = min(abs(left[0] - right[0]) + abs(left[1] - right[1]), result)

print(result)
