"""
https://www.acmicpc.net/problem/10866
"""

from collections import deque
import sys

t = int(sys.stdin.readline().rstrip())

queue = deque()

for _ in range(t):
    n = sys.stdin.readline().rstrip().split()

    if n[0] == "push_back":
        queue.append(n[1])
    elif n[0] == "push_front":
        queue.appendleft(n[1])
    elif n[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif n[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif n[0] == "size":
        print(len(queue))
    elif n[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif n[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif n[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
