"""
https://www.acmicpc.net/problem/9466
dfs 방식 비슷해보이는데 시간 초과가 안남
대부분이 dfs 방식으로 풀었으며 pypy3로 답안을 제출 약간 타이트한 문제인듯
"""

import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
t = int(sys.stdin.readline().rstrip())


def dfs(start):
    global result
    visited[start] = 1
    team.append(start)

    next_pos = graph[start]

    if visited[next_pos] == 1:
        if next_pos in team:
            result += len(team[team.index(next_pos) : ])
        return
    else :
        dfs(next_pos)


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    graph = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [0] * len(graph)
    result = 0
    for i in range(1, len(graph)):
        if visited[i] == 0:
            team = []
            dfs(i)
    print(n - result)

"""
https://www.acmicpc.net/problem/9466
bfs 방식으로 풀었을 때는 시간초과 발생
"""

import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())


def bfs(start, graph, visited):
    if visited[start] == 2 or visited[start] == 1:
        return

    visited[start] = 1
    que = deque()
    que.append(graph[start])
    temp_visited = []
    temp_visited.append(start)

    while que:
        idx = que.popleft()
        if idx == start:
            for i in temp_visited:
                visited[i] = 2
            return
        else:
            if idx in temp_visited:
                for i in range(temp_visited.index(idx), len(temp_visited)):
                    visited[temp_visited[i]] = 2
                return
            temp_visited.append(idx)
            que.append(graph[idx])

    return


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    graph = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [0] * len(graph)

    for i in range(1, len(graph)):
        bfs(i, graph, visited)
    print(visited.count(1))