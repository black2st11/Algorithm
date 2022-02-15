"""
https://www.acmicpc.net/problem/14502

해당 부분은 python으로 돌렸을 때 시간 초과가 무조건 나기에(맵 부분을 카피 혹은 새로 작성 혹은 기둥 부분과 바이러스 부분 위치 값 저장 후 생성)
pypy3 로 돌림
"""
import sys
from collections import deque
import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, sys.stdin.readline().rstrip().split())
lab = []

for _ in range(n):
    lab.append(list(map(int, sys.stdin.readline().rstrip().split())))


def bfs():
    copy_lab = copy.deepcopy(lab)
    que = deque()

    for i in range(n):
        for j in range(m):
            if copy_lab[i][j] == 2:
                que.append([i, j])

    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < n and ny >= 0 and nx < m and nx >= 0:
                if copy_lab[ny][nx] == 0:
                    copy_lab[ny][nx] = 2
                    que.append([ny, nx])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if copy_lab[i][j] == 0:
                cnt += 1
    return cnt


maximum = 0


def make_wall(step):
    global maximum
    if step == 3:
        rst = bfs()
        maximum = max(maximum, rst)
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(step + 1)
                lab[i][j] = 0


make_wall(0)

print(maximum)
