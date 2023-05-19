"""
https://www.acmicpc.net/problem/1260
"""

import sys
from collections import deque


def dfs(x, graph, visited):
    visited[x] = 1
    print(x, end=" ")
    for i in range(1, len(graph)):
        if graph[x][i] == 1 and visited[i] != 1:
            dfs(i, graph, visited)


def bfs(x, graph, visited):
    que = deque()
    que.append(x)
    visited[x] = 1
    while que:
        item = que.popleft()
        print(item, end=" ")
        for i in range(len(graph)):
            if graph[item][i] == 1 and visited[i] == 0:
                que.append(i)
                visited[i] = 1


ini = list(map(int, sys.stdin.readline().rstrip().split()))

graph = [[0] * (ini[0] + 1) for _ in range(ini[0] + 1)]
visited = [0] * (ini[0] + 1)

for _ in range(ini[1]):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    graph[n][m] = 1
    graph[m][n] = 1
dfs(ini[2], graph[:], visited[:])
print()
bfs(ini[2], graph[:], visited[:])
