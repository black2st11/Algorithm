n, m = map(int, input().split(' '))

array = []

for _ in range(n):
    array.append(list(map(int, input().split(' '))))
    
def ice_check(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if array[x][y] == 0:
        array[x][y] = 1
        ice_check(x-1, y)
        ice_check(x+1, y)
        ice_check(x, y-1)
        ice_check(x, y+1)
        return True
    return False


count = 0

for i in range(n):
    for j in range(m):
        if ice_check(i, j):
            count += 1

print(count)