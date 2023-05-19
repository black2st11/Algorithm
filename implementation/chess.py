'''
나이트가 이동할 수 있는 가지 수를 구하여라
이동하는 방식은 두가지가 있다.
1. 수평으로 2칸 이동 후 수직 이동 1칸
2. 수직으로 2칸 이동 후 수평 이동 1칸 
'''

position = input()
column = int(ord(position[0])) - int(ord('a')) + 1
row = int(position[1])

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, -2)]

count = 0 

for step in steps :
    next_row = row + step[0]
    next_column = row + step[1]

    if next_row >=1 and next_column >= 1 and next_row <= 8 and next_column <= 8:
        count += 1
print(count)