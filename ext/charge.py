'''
백준 23843
'''
from collections import deque
import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())

k = list(map(int, sys.stdin.readline().rstrip().split()))
k.sort(reverse=True)

deq = deque(k)
result = 0
stack = []

while deq:
    for _ in range(n):
        if len(stack) < m and deq : 
            stack.append(deq.popleft())
        else:
            break
    low_time = min(stack)
    low_count = 0
    
    for i in range(len(stack)):
        stack[i] -= low_time
        if stack[i] == 0:
            low_count +=1
            
    result += low_time
    for _ in range(low_count):
        stack.pop()
if stack:
    result += max(stack)
print(result)
