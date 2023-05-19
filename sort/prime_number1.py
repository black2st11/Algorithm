'''
백준 1978
'''
import sys

n = int(sys.stdin.readline().rstrip())

m = list(map(int, sys.stdin.readline().rstrip().split()))

array = [0] * 1001
array[1] = 1
array[0] = 1


for i in range(2, 1001):
    for j in range(2, 500):
        if i * j >= 1001:
            break
        array[i * j] = 1
answer = 0
for i in m :
    if array[i] == 0:
        answer += 1

print(answer)