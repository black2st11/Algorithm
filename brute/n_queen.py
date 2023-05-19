"""
https://www.acmicpc.net/problem/9663

n = 5
[0, 0, 0, 0, 0]
이런 가정으로 인덱스가 row(step)
arr[row] => col 느낌으로 (N) 
기존 [ROW, COL] 개념에서 줄임 (N^2) 
"""
import sys

n = int(sys.stdin.readline().rstrip())


picked = [0] * n


def check_queen(row, col):
    for prev in range(row):
        if picked[prev] == col:
            return False

        if abs(picked[prev] - col) == row - prev:
            return False

    return True


cnt = 0


def put_queen(step):
    global cnt
    if step == n:
        cnt += 1
        return

    for i in range(n):
        if check_queen(step, i):
            picked[step] = i
            put_queen(step + 1)


put_queen(0)
print(cnt)
