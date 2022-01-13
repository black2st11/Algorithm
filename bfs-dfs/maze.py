from collections import deque
n, m = map(int, input().split(' '))

array = []
for _ in range(n):
    array.append(list(map(int, input().split(' '))))

dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]

def go(x,y):
    deq = deque()
    deq.append((x, y))
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if array[nx][ny] == 0 :
                continue
            
            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                deq.append((nx, ny))

    return array[n-1][m-1]
print(go(0 ,0))