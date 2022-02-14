"""
https://www.acmicpc.net/problem/1436
그냥 무식하게 모든 숫자에 대해서 함
"""
import sys

n = int(sys.stdin.readline().rstrip())

array = []
i = 665
while len(array) != n:
    i += 1
    if "666" in str(i):
        array.append(i)

print(array[n - 1])

