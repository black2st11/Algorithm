import sys
from collections import deque

deq = deque()
result = 0
n, m = map(int, sys.stdin.readline().rstrip().split())


def left_rotate(deq):
    deq.append(deq.popleft())


def right_rotate(deq):
    deq.appendleft(deq.pop())


for i in range(1, n + 1):
    deq.append(i)

targets = list(map(int, sys.stdin.readline().rstrip().split()))

for target in targets:
    if deq.index(target) > len(deq) // 2:
        while deq[0] != target:
            result += 1
            right_rotate(deq)
    else:
        while deq[0] != target:
            result += 1
            left_rotate(deq)
    deq.popleft()
print(result)
