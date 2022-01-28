"""
https://www.acmicpc.net/problem/11724
"""
import sys

sys.setrecursionlimit(10000)


def dfs(graph, v, visited):
    if visited[v] == 0:
        visited[v] = 1
    else:
        return 0
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

    return 1


n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

for i in range(1, len(graph)):
    count += dfs(graph, i, visited)

print(count)
