from dis import dis
import heapq
import sys

INF = int(1e9)

n, m, c = map(int, sys.stdin.readline().rstrip().split())

distance = [INF] * (n + 1)
graph = [[] for _ in range(n+1)]

distance[c] = 0

for i in range(m):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    
    graph[x].append((y,z))

q = []
heapq.heappush(q, (0, c))

while q:
    item = heapq.heappop(q)
    for node in graph[item[1]]:
        if distance[node[0]] > distance[item[1]] + node[1]:
            distance[node[0]] = distance[item[1]] + node[1]
        heapq.heappush(q, (node[1], node[0]))

for j in graph:
    print(j)

print(distance)

count = 0
for j in distance[1:]:
    if j >0:
        count += 1
print(count, max(distance[1:]))
