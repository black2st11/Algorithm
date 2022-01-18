import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[INF] * (n+1) for i in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

x, k = map(int, sys.stdin.readline().rstrip().split())

answer = -1 if graph[1][k] + graph[k][x] >= INF else graph[1][k] + graph[k][x]

print(answer)