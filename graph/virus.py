"""
https://www.acmicpc.net/problem/2606
"""

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

k = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = True
    while que:
        node = que.popleft()
        for v in graph[node]:
            if visited[v] == False:
                visited[v] = True
                que.append(v)


bfs(1)

print(visited.count(True) - 1)
