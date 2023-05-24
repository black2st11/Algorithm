import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    side = True
    command = sys.stdin.readline().rstrip()
    length = int(sys.stdin.readline().rstrip())
    array = sys.stdin.readline().rstrip()
    array = array[1:-1].split(",")
    array = deque(array)
    if "" in array:
        array.remove("")
    for com in command:
        if com == "R":
            side = not side
        else:
            if len(array) == 0:
                print("error")
                break
            if side:
                array.popleft()
            else:
                array.pop()
    else:
        if not side:
            array.reverse()

        print("[" + ",".join(array) + "]")
