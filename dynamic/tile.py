"""
백준 11727
"""
import sys

n = int(sys.stdin.readline().rstrip())

array = [0] * 1001

array[1] = 1
array[2] = 3

for i in range(3, n + 1):
    array[i] = (array[i - 1] + array[i - 2] * 2) % 10007

print(array[n])
