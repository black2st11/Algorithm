"""
https://www.acmicpc.net/problem/1992
"""

import sys

n = int(sys.stdin.readline())

array = [sys.stdin.readline().rstrip() for _ in range(n)]


def count_array(x, y, n):
    check_num = array[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check_num != array[i][j]:
                print("(", end="")
                for k in range(2):
                    for l in range(2):
                        count_array(x + k * n // 2, y + l * n // 2, n // 2)
                print(")", end="")

                return
    print(check_num, end="")


count_array(0, 0, n)

