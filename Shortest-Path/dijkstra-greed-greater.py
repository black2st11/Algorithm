import heapq
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

start = int(sys.stdin.readline().rstrip())

graph = [[] for _  in range(n + 1)]

distance = [999999] * (n+1)
distance[start] = 0

for i in range(m):
    # a start_node, b target_node, c distance
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

q = []
heapq.heappush(q,(0, start))

while q:
    item = heapq.heappop(q)

    if distance[item[1]] < item[0]:
        continue

    for node in graph[item[1]]:
        if distance[node[0]] > node[1] + distance[item[1]]:
            distance[node[0]] = node[1] + distance[item[1]]
            heapq.heappush(q, (distance[node[0]], node[0]))

for i in range(1, n+1):
    a = -1 if distance[i] == 999999 else distance[i]
    print(a)