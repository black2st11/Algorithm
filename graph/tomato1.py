"""
https://www.acmicpc.net/problem/7569
3차원이네 ...
해당 문제는 제대로 풀었는데 dz -1은 넣고 1을 빼 먹어서 실패함
심지어 테스트 케이스는 그 상태로 해도 다 맞아서 더욱 더 뭐가 틀린지 몰랐는데
그냥 전체 배열 찍어보니까 z 가 안 움직이는 것 보고 발견
pypy로도 돌아가고 python으로도 돌아감
"""
import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().rstrip().split())


dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]


arr = []

for i in range(h):
    temp = []
    for i in range(n):
        temp.append(list(map(int, sys.stdin.readline().rstrip().split())))
    arr.append(temp)


def bfs():
    que = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if arr[z][y][x] == 1:
                    que.append((z, y, x, 0))

    while que:
        z, y, x, hour = que.popleft()

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if nz >= h or nz < 0 or ny >= n or ny < 0 or nx >= m or nx < 0:
                continue

            if arr[nz][ny][nx] == 1 or arr[nz][ny][nx] == -1:
                continue

            arr[nz][ny][nx] = 1

            que.append((nz, ny, nx, hour + 1))

    for z in range(h):
        for y in range(n):
            for x in range(m):
                if arr[z][y][x] == 0:
                    print(-1)
                    return
    else:
        print(hour)


bfs()
