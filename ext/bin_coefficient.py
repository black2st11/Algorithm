"""
https://www.acmicpc.net/submit/11050
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = [0] * 11

arr[1] = 1

for i in range(2, len(arr)):
    arr[i] = i * arr[i - 1]
if n == m:
    print(1)
elif m == 0:
    print(1)
else:
    print(arr[n] // (arr[m] * (arr[n - m])))

