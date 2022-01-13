'''
1. N * M 배열이 있으며 현재 위치는 x, y 이다 바라보는 처음바라보는 방향은 남쪽이다.
2. 0은 이동이 가능한 곳, 1은 이동이 불가한 곳이다.
3. 바라보는 방향으로 진행이 가능한 경우 해당하는 방식을 우선하고 왼쪽회전 후 이동, 오른쪽 회전 후 이동, 뒤로 회전 후 이동하는 방식 순으로 우선순위를 가진다.
4. k번 만큼 이동한 후 해당하는 위치의 좌표를 표현해라
'''

n, m = map(int, input().split(' '))

x, y = map(int, input().split(' '))

# 0은 남쪽, 1은 동쪽, 2는 북쪽, 3은 서쪽
direction = 0 
direction_range = [0, 1, 2, 3]


dx = [1, 0, -1, 0]
dy = [0, 1 , 0, -1]
array = []
for _ in range(n):
	array.append(list(map(int, input().split(' '))))

k = int(input())

rotate = [0, 1, -1, -2]
for _ in range(k):
    for i in rotate:
        if direction + i > 3:
            next_direction = 0
        else :
            next_direction = direction_range[direction + i]

        if array[x+dx[next_direction]][y+dy[next_direction]] == 0:
            x += dx[next_direction]
            y += dy[next_direction]
            direction = next_direction
            break
    
print(x, y) 
    

             