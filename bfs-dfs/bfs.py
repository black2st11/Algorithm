from collections import deque

def bfs(graph, v, visited):
    deq = deque([v])
    visited[v] = True
    while deq:
        i = deq.popleft()
        print(i, end=' ')
        for item in graph[i]:
            if not visited[item] :
                deq.append(item)
                visited[item] = True

graph = [
    [],
    [2, 3 ,8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)