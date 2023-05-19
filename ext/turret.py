'''
백준 1002
'''
import sys
import math

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
    if distance == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0)  # 그 외에

