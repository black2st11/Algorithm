import heapq
import sys

n = int(sys.stdin.readline().rstrip())
q = []

for _ in range(n):

    num = int(sys.stdin.readline().rstrip())

    if num == 0:
        try:
            item = heapq.heappop(q)
            print(item)
        except:
            print(0)
    else:
        heapq.heappush(q, num)

