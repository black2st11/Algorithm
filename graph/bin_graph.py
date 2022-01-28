import sys

t = int(sys.stdin.readline().rstrip())


def dfs(graph, v, visited, flag):
    visited[v] = flag

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, -flag)


for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())

    graph = [[] for i in range(n + 1)]
    visited = [0] * (n + 1)
    first = 0
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if first == 0:
            first = a
        graph[a].append(b)
        graph[b].append(a)

    dfs(graph, first, visited, 1)

    prev = -1

    print(
        "YES"
        if all(
            all(visited[i] == -visited[j] for j in graph[i]) for i in range(1, n + 1)
        )
        else "NO"
    )
