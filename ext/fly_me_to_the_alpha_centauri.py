'''
백준 1011
'''
import sys
import math
t = int(sys.stdin.readline().rstrip())

result= []

for i in range(t):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    distance = y - x
    
    n = round(math.sqrt(float(distance)))

    if distance <= n**2 :
        result.append(2*n-1)
    else:
        result.append(2*n) 
for i in result:
    print(i)