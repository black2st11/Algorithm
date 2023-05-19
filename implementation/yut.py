"""
https://www.acmicpc.net/problem/2490

등의 개수는 리스트의 원소를 더한 경우로 알 수 있음
"""
import sys

arr = ["E", "A", "B", "C", "D"]

for i in range(3):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    print(arr[4 - sum(a)])
