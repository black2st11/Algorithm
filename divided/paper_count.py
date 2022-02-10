"""
https://www.acmicpc.net/problem/1780
"""
import sys

a = int(sys.stdin.readline().rstrip())

array = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(a)]

result = [0, 0, 0]


def count_array(x, y, n):
    global result
    num_check = array[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if array[i][j] != num_check:
                for k in range(3):
                    for l in range(3):
                        count_array(x + k * n // 3, y + l * n // 3, n // 3)
                return

    if num_check == -1:
        result[0] += 1
    elif num_check == 0:
        result[1] += 1
    elif num_check == 1:
        result[2] += 1


count_array(0, 0, a)

for i in result:
    print(i)
