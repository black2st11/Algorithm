import sys
from collections import deque

que = deque()
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()

    if len(command) > 1:
        que.append(command[1])
    elif command[0] == "front":
        print(que[0] if len(que) else -1)
    elif command[0] == "back":
        print(que[-1] if len(que) else -1)
    elif command[0] == "size":
        print(len(que))
    elif command[0] == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif command[0] == "empty":
        print(1 if len(que) == 0 else 0)
