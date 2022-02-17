"""
https://www.acmicpc.net/problem/11279

heapq 에서 우선 순위를 바꿀 수 있는 지 모르니까 -1 곱해서 저장 후 뺄때는 -1 곱해서 원래 상태로
"""

import sys
import heapq

n = int(sys.stdin.readline().rstrip())


q = []
for _ in range(n):
    m = int(sys.stdin.readline().rstrip())

    if m == 0:
        if q:
            a = heapq.heappop(q)
            print(a * -1)
        else:
            print(0)
    else:
        heapq.heappush(q, m * -1)
