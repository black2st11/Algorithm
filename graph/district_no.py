"""
https://www.acmicpc.net/problem/2667
"""
import sys

n = int(sys.stdin.readline().rstrip())

graph = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    temp_list = []
    for i in word:
        temp_list.append(int(i))
    graph.append(temp_list)


def dfs(row, col):
    if graph[row][col] == 0:
        return 0

    graph[row][col] = 0
    temp = 0
    for i in range(4):
        if row + dy[i] >= n or col + dx[i] >= n or row + dy[i] < 0 or col + dx[i] < 0:
            continue
        temp += dfs(row + dy[i], col + dx[i])
    return temp + 1


result = 0
result_list = []
for i in range(n):
    for j in range(n):
        res = dfs(i, j)
        if not res == 0:
            result += 1
            result_list.append(res)

print(result)

result_list.sort()
for i in result_list:
    print(i)
