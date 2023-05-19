"""
https://www.acmicpc.net/problem/3190
"""
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

maps = [[0] * n for _ in range(n)]


apple_count = int(sys.stdin.readline().rstrip())


for _ in range(apple_count):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    maps[x - 1][y - 1] = 1

spell_count = int(sys.stdin.readline().rstrip())
spells = []

for _ in range(spell_count):
    spells.append(sys.stdin.readline().rstrip().split())

second = 0
x = 1
y = 1

snake = deque()
snake.append((x, y))

# 0은 동, 1은 남, 2는 서, 3은 북

direction = 0

# x는 행, y는 열
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
maps[x - 1][y - 1] = 2

while True:
    second += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx <= n and nx > 0 and ny <= n and ny > 0 and maps[nx - 1][ny - 1] != 2:
        if maps[nx - 1][ny - 1] == 1:
            maps[nx - 1][ny - 1] = 2
        else:
            px, py = snake.pop()
            maps[px - 1][py - 1] = 0

        snake.appendleft((nx, ny))
        maps[nx - 1][ny - 1] = 2

        x = nx
        y = ny
    else:
        break

    for spell in spells:
        if int(spell[0]) == second:
            if spell[1] == "L":
                direction = 3 if direction - 1 < 0 else direction - 1
            else:
                direction = 0 if direction + 1 > 3 else direction + 1

print(second)
