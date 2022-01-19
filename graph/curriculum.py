import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

indeed = [0] * (n+1)
courses = [[] for _ in range(n+1)]
time = [0] * (n+1)

for i in range(1, n+1):
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(array)):
        if j == 0:
            time[i] = array[j]
        elif array[j] == -1:
            break 
        else :
            indeed[i] += 1
            courses[array[j]].append(i)
    
answer = time[:]

que = deque()

for i in range(1, n+1):
    if indeed[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    
    for i in courses[now]:
        indeed[i] -= 1
        answer[i] = max(answer[i], answer[now] + time[i])
        if indeed[i] == 0 :
            que.append(i)


print(time)
print(answer)