import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

start = int(sys.stdin.readline().rstrip())

graph = [[] for _  in range(n + 1)]


visited = [False] * (n + 1)
visited[0] = [True]

distance = [999999] * (n+1)
distance[start] = 0

for i in range(m):
    # a start_node, b target_node, c distance
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))


def find_smallest_distance():
    min_value = 999999
    index = 0
    for j in range(n+1):
        if min_value > distance[j] and not visited[j] :
            min_value = distance[j]
            index = j
    return index

for node in graph[start]:

    if distance[node[0]] > node[1] + distance[start]:
        distance[node[0]] = node[1] + distance[start]

for i in range(n-1):
    index = find_smallest_distance()

    visited[index] = True
    for node in graph[index]:
        if distance[node[0]] > node[1] + distance[index]:
            distance[node[0]] =  node[1] + distance[index]

for i in range(1, n+1):
    a = -1 if distance[i] == 999999 else distance[i]
    print(a)