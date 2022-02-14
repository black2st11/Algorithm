"""
https://www.acmicpc.net/problem/2748, 2747
"""
import sys

n = int(sys.stdin.readline().rstrip())

if n <= 1:
    print(n)
else:
    array = [0] * (n + 1)

    array[0] = 0
    array[1] = 1

    for i in range(2, n + 1):
        array[i] = array[i - 1] + array[i - 2]

    print(array[-1])
