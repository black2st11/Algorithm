"""
https://www.acmicpc.net/problem/10451
"""

import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())


def bfs(start, graph, visited):
    if visited[start] == 1:
        return 0

    que = deque()
    que.append(graph[start])
    visited[start] = 1

    while que:
        idx = que.popleft()
        visited[idx] = 1
        next_idx = graph[idx]

        if visited[next_idx] == 0:
            que.append(next_idx)

    return 1


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    array = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [0] * (len(array))

    result = 0
    for i in range(1, len(array)):
        result += bfs(i, array, visited)

    print(result)
