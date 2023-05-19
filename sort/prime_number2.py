'''
백준 2581
'''

import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

array = [0] * 10001
array[1] = 1
array[0] = 1


for i in range(2, 10001):
    for j in range(2, 5000):
        if i * j >= 10001:
            break
        array[i * j] = 1


answer = 0
min_value = int(1e9)

for i in range(n, m+1) :
    if array[i] == 0:
        answer += i
        if min_value > i:
            min_value = i

if answer == 0:
    print(-1)
else: 
    print(answer)
    print(min_value)