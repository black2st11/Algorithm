"""
https://www.acmicpc.net/problem/9466
수정 예정
"""

import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())


def bfs(start, graph, visited):
    if visited[start] == 2 or visited[start] == 1:
        return

    visited[start] = 1
    que = deque()
    que.append(graph[start])
    temp_visited = []
    temp_visited.append(start)

    while que:
        idx = que.popleft()
        if idx == start:
            for i in temp_visited:
                visited[i] = 2
            return
        else:
            if idx in temp_visited:
                for i in range(temp_visited.index(idx), len(temp_visited) + 1):
                    visited[i] = 2
                return
            temp_visited.append(idx)
            que.append(graph[idx])

    return


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    graph = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [0] * len(graph)

    for i in range(1, len(graph)):
        bfs(i, graph, visited)
    print(visited.count(1))
