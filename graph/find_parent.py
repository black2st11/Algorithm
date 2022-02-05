"""
https://www.acmicpc.net/problem/11725
"""

import sys

sys.setrecursionlimit(int(1e9))

n = int(sys.stdin.readline().rstrip())

graph = []

for i in range(n + 1):
    graph.append([])

parent = [0, 1] + [0] * (n - 1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):

    for i in graph[start]:
        if parent[start] == i:
            continue

        if parent[i] == 0:
            parent[i] = start
        dfs(i)


dfs(1)

for i in range(2, len(parent)):
    print(parent[i])
