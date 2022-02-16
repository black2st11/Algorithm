import sys
from collections import deque

q = deque()

n, m = map(int, sys.stdin.readline().rstrip().split())

for i in range(1, n + 1):
    q.append(i)

cnt = 0

arr = []
while q:
    cnt += 1
    if cnt == m:
        arr.append(str(q.popleft()))
        cnt = 0
    else:
        q.rotate(-1)

print("<" + ", ".join(arr) + ">")
