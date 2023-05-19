"""
https://www.acmicpc.net/problem/1037
"""
import sys

n = sys.stdin.readline().rstrip()

arr = list(map(int, sys.stdin.readline().rstrip().split()))

print(min(arr) * max(arr))
