"""
https://www.acmicpc.net/problem/14889
combination 안 쓰고 풀려고 하니까 시간 초과 나서 pypy3 로 품
"""

import sys

n = int(sys.stdin.readline().rstrip())

player = []

result = int(1e9)

picked = [False] * n

for _ in range(n):
    player.append(list(map(int, sys.stdin.readline().rstrip().split())))


def calulate(picked):
    global result
    picked_team = 0
    remain_team = 0
    for i in range(n):
        for j in range(n):
            if picked[i] == picked[j]:
                if picked[i]:
                    picked_team += player[i][j]
                else:
                    remain_team += player[i][j]

    result = min(result, abs(picked_team - remain_team))


def pick(step, idx):
    if step == n // 2:
        calulate(picked)
        return
    for i in range(idx, n):
        if picked[i] == True:
            continue
        picked[i] = True
        pick(step + 1, i + 1)
        picked[i] = False


pick(0, 0)
print(result)
