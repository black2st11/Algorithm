"""
https://www.acmicpc.net/problem/1167
메모리 초과(인접행렬)
"""

# import sys

# sys.setrecursionlimit(int(1e9))
# n = int(sys.stdin.readline().rstrip())

# INF = int(1e9)

# tree = [[INF] * (n + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     li = list(map(int, sys.stdin.readline().rstrip().split()))

#     for j in range(1, len(li), 2):
#         if li[j] == -1:
#             continue
#         else:
#             tree[i][li[j]] = li[j + 1]


# for k in range(1, len(tree)):
#     for a in range(1, len(tree)):
#         for b in range(1, len(tree)):
#             if a == b:
#                 continue
#             tree[a][b] = min(tree[a][b], tree[a][k] + tree[k][b])

# result = 0

# for i in range(1, len(tree)):
#     for j in range(1, len(tree)):
#         if tree[i][j] != INF:
#             result = max(result, tree[i][j])

# print(result)

"""
다익스트라dfs 방식 시간 초과
"""
# tree = [[] * (n + 1) for _ in range(n + 1)]


# for i in range(1, n + 1):
#     li = list(map(int, sys.stdin.readline().rstrip().split()))

#     for j in range(1, len(li), 2):
#         if li[j] == -1:
#             continue
#         else:
#             tree[i].append([li[j], li[j + 1]])


# def max_path(start):
#     visited[start] = 1
#     distance = 0
#     for item in tree[start]:
#         vertex = item[0]
#         edge = item[1]

#         if visited[vertex] == 1:
#             continue

#         distance = max(edge + max_path(vertex), distance)

#     return distance


# result = 0
# for i in range(1, len(tree)):
#     visited = [0] * (n + 1)
#     result = max(max_path(i), result)
# print(result)


"""
참고용
"""
from sys import stdin
from collections import deque

read = stdin.readline
V = int(read())
graph = [[] for _ in range(V + 1)]

for _ in range(V - 1):
    c = list(map(int, read().split()))
    graph[c[0]].append((c[1], c[2]))


def bfs(start):
    visit = [-1] * (V + 1)
    que = deque()
    que.append(start)
    visit[start] = 0
    _max = [0, 0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                que.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e

    return _max


dis, node = bfs(1)
dis, node = bfs(node)
print(dis)
