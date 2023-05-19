'''
백준 1929
'''

# 이 방식은 타임아웃(구간이 짧으면 얘가 더 빠를가능성이 있음)
import sys
import math
n, m = map(int,sys.stdin.readline().rstrip().split())

for i in range(n, m+1) :
    flag = True
    for j in range(2, math.ceil(math.sqrt(i))+1):
        if i % j == 0:
            flag = False
    else : 
        if flag :
            print(i)

# 다른 방식
n, m = map(int,sys.stdin.readline().rstrip().split())

array = [0] * 1000001
array[1] = 1
array[0] = 1


for i in range(2, 1000001):
    for j in range(2, 500001):
        if i * j >= 1000001:
            break
        array[i * j] = 1



for i in range(n, m+1) :
    if array[i] == 0:
        print(i)