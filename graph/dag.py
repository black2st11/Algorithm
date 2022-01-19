import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

indeed = [0] * (n + 1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    indeed[b] += 1


deq = deque()

result = []

for i in range(1, n+1):
    if indeed[i] == 0:
        deq.append(i)

while deq:
    i = deq.popleft()
    for j in graph[i]:
        indeed[j] -= 1

        if indeed[j] == 0:
            deq.append(j)

    result.append(i)

for i in result:
    print(i , end= ' ')