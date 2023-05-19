import sys
from collections import deque

que = deque()

n = int(sys.stdin.readline().rstrip())


for i in range(1, n + 1):
    que.append(i)


while len(que) != 1:
    que.popleft()
    que.rotate(-1)
print(que[0])
