'''
n * n 크기의 정사각형 공간 위에 서 있다.
이동할 수 있는 거리는 1칸이며
상 하 좌 우 로 이동이 가능하다.
입력되어지는 방향으로 이동 후 마지막의 위치를 표시한다.
시작되는 위치는 (1,1) 이다.
'''

n = int(input())
array = input().split(' ')
position = [1,1]

for i in array:
    if i == 'L':
        if position[1] - 1 > 0 :
            position[1] -= 1
    if i == 'R': 
        if position[1] + 1 <= n :
            position[1] += 1
    if i == 'U':
        if position[0] - 1 > 0 :
            position[0] -= 1
    if i == 'D':
        if position[0] + 1 <= n:
            position[0] += 1

print(position)