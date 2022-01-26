"""
https://www.acmicpc.net/problem/1406
"""
import sys

left = list(sys.stdin.readline().rstrip())
right = []
t = int(sys.stdin.readline().rstrip())


for i in range(t):
    n = sys.stdin.readline().rstrip().split()
    if n[0] == "P":
        left.append(n[1])
    elif n[0] == "B":
        if left:
            left.pop()
        continue
    elif n[0] == "L":
        if left:
            right.append(left.pop())
    elif n[0] == "D":
        if right:
            left.append(right.pop())

print("".join(left + right[::-1]))
