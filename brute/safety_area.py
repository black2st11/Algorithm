"""
https://www.acmicpc.net/problem/2468

처음에 문제를 이해 못해서 헤멤 영역의 크기로 생각하고 예제를 보는데 크기로 보면 6인데 답이 5라고 하길래 나중에 영역의 개수임을 이해함

min_height - 1을 하는 이유는 비가 아예 안온다라고 생각할 수도 있지만
최소 높이에서 -1 만 되어도 안온걸로 생각할 수 있기에 0에서 시작보다 최소 높이에서 -1 한 부분부터 시작
"""

import sys
from collections import deque
import copy


n = int(sys.stdin.readline().rstrip())
arr = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

min_height = int(1e9)
max_height = 0

for _ in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    min_height = min(min_height, min(a))
    max_height = max(max_height, max(a))
    arr.append(a)


def bfs(i, j, height, arr):
    if arr[i][j] <= height:
        return 0

    q = deque()
    q.append([i, j])

    while q:
        y, x = q.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= n or ny < 0 or nx >= n or nx < 0:
                continue

            if arr[ny][nx] <= height:
                continue

            arr[ny][nx] = 0
            q.append([ny, nx])
    return 1


rst = 0
for k in range(min_height - 1, max_height):
    cnt = 0
    b = copy.deepcopy(arr)

    for i in range(n):
        for j in range(n):
            cnt += bfs(i, j, k, b)
    rst = max(cnt, rst)

print(rst)


### 이해용도 잠깐 봤을 때 느낌은 각각의 집합을 합치는 느낌? 그래서 루트 개수 계산?

import sys
from collections import defaultdict as dd

input = sys.stdin.readline


# 루트 찾는 느낌???
def Repr(a):
    if Set[a] == a:
        return a
    k = Repr(Set[a])
    Set[a] = k
    return k


# 루트 합치는 느낌?
def Join(a, b):
    Set[Repr(b)] = Repr(a)


def adj(p):
    yield p - w
    yield p - 1
    yield p + 1
    yield p + w


n = int(input())
w = n + 2

Set = {}

contour = dd(list)
for i in range(1, n + 1):
    new = list(map(int, input().split()))
    for h, j in zip(new, range(i * w + 1, (i + 1) * w - 1)):
        contour[h].append(j)
heights = sorted(contour, reverse=True)
heights.pop()
fixed = []
cnt = 1
for h in heights:
    for k in contour[h]:
        Set[k] = k
    for p in contour[
        h
    ]:  # Connection change is made from added points(to both new and old components)
        for q in adj(p):
            if q in Set:
                Join(p, q)
    fixed = [p for p in fixed if Set[p] == p]
    for p in contour[h]:
        if Set[p] == p:
            fixed.append(p)
    cnt = max(cnt, len(fixed))

print(cnt)
