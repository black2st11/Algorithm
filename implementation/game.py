'''
N * M 형식의 지도가 있다.
진행방향은 바라보는 방향에서 왼쪽방향으로 이동이 가능할 경우 해당 방향으로 이동한다.
이동이 가능한 경우는 땅이거나 가지않은 곳일 경우이다.
해당 위치에서 갈 수 있는 곳이 없을 경우 뒤로 진행하고 위의 방법을 진행하고 뒤로도 갈 수 있는 곳이 없을 경우 프로그램을 종료하고 최종적으로 방문한 칸의 개수를 나타낸다.
'''

n, m = map(int,input().split(' '))

is_gone = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y , direction = map(int, input().split(' '))

is_gone[x][y] = 1

array = []
for _ in range(n):
    array.append(list(map(int, input().split(' '))))

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_count = 0
while True:
    turn_left()

    next_x = x + dx[direction]
    next_y = y + dy[direction]

    if array[next_x][next_y] == 0 and is_gone[next_x][next_y] == 0:
        x = next_x
        y = next_y
        turn_count = 0
        count += 1
        is_gone[x][y] = 1

        continue
    else :
        turn_count += 1

    if turn_count == 4:
        prev_x = x - dx[direction]
        prev_y = y - dy[direction]
        
        if array[prev_x][prev_y] == 0:
            x = prev_x
            y = prev_y
            turn_count = 0

        else :
            break
        turn_time = 0

print(count)