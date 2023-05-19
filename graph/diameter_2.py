"""
https://www.acmicpc.net/problem/1967

dfs bfs
dfs는 개선이 필요하기는 함 원래 예상은 단말노드에 갔을 때의 값을 저장해야하는데 그렇지 못함 이 부분 수정 필요
"""
# bfs dfs
import sys
from collections import deque

sys.setrecursionlimit(int(1e9))

n = int(sys.stdin.readline().rstrip())

visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    visited
    graph[a].append([b, c])
    graph[b].append([a, c])
temp_1 = []


def find_max_by_dfs(start, w):
    _max = [start, w]
    if visited[start] == 0:
        visited[start] = 1
        for item in graph[start]:
            vertex = item[0]
            distance = item[1]
            if visited[vertex] == 1:
                temp_1.append([start, w])
            result = find_max_by_dfs(vertex, distance + w)
            if _max[1] < result[1]:
                _max = result

    return _max


def find_max_by_bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    que = deque()
    que.append(start)
    _max = [0, 0]

    while que:
        node = que.popleft()
        for item in graph[node]:
            vertex = item[0]
            distance = item[1]
            if visited[vertex] == -1:
                visited[vertex] = distance + visited[node]
                que.append(vertex)
                if _max[1] < visited[vertex]:
                    _max = vertex, visited[vertex]
    return _max


node, dis = find_max_by_dfs(1, 0)
temp_1.sort(key=lambda x: -x[1])

if not temp_1:
    print(0)
else:
    node, dis = temp_1[0]
    temp_1 = []
    visited = [0] * (n + 1)
    find_max_by_dfs(node, 0)
    temp_1.sort(key=lambda x: -x[1])
    print(temp_1[0][1])
