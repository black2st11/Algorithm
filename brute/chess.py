"""
https://www.acmicpc.net/problem/1018

처음에 문제를 잘 못 이해해서 분할 이후에 색칠 한 후 다시 붙이고 하는 과정을 반복해서 최솟값인 줄 알았는데
한번 분할 했을 때 최소한으로 칠하는 경우를 구하라 해서 헤멤
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = []

for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

patt1 = "WBWBWBWB"
patt2 = "BWBWBWBW"

board1 = [patt1, patt2, patt1, patt2, patt1, patt2, patt1, patt2]
board2 = [patt2, patt1, patt2, patt1, patt2, patt1, patt2, patt1]
result = int(1e9)
for i in range(n - 7):
    for j in range(m - 7):
        cnt_1 = 0
        cnt_2 = 0
        for k in range(8):
            for l in range(8):
                if arr[i + k][j + l] != board1[k][l]:
                    cnt_1 += 1
                elif arr[i + k][j + l] != board2[k][l]:
                    cnt_2 += 1

        result = min(result, cnt_1, cnt_2)

print(result)
