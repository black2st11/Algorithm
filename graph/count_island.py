"""
https://www.acmicpc.net/problem/4963
"""
import sys

sys.setrecursionlimit(100000)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(row, col):
    if graph[row][col] == 0:
        return 0

    graph[row][col] = 0
    temp = 0
    for i in range(-1, 2, 1):
        if row + i >= h or row + i < 0:
            continue
        for j in range(-1, 2, 1):
            if col + j >= w or col + j < 0:
                continue
            temp += dfs(row + i, col + j)

    return 1


while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    graph = []

    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    result = 0
    for i in range(h):
        for j in range(w):
            result += dfs(i, j)

    print(result)
