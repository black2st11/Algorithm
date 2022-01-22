"""
백준 2193
"""
import sys

n = int(sys.stdin.readline().rstrip())

array = [0] * 91
array[1] = 1
array[2] = 1

for i in range(3, 91):
    array[i] = array[i - 2] + array[i - 1]

print(array[n])
