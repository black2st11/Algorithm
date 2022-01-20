'''
백준 9020
'''
import sys
import math

n = int(sys.stdin.readline().rstrip())

question = []
for _ in range(n):
    m = int(sys.stdin.readline().rstrip())
    question.append(m)

array = [0] * 10001
array[1] = 1
array[0] = 1


for i in range(2, 10001):
    for j in range(2, 5000):
        if i * j >= 10001:
            break
        array[i * j] = 1
MAX = int(1e9)
answer = [[0, MAX] for _ in range(n)]

turn = 0
for i in question :
    for j in range(2, math.ceil(i/2) + 1):
        if array[j] == 0 and array[i-j] == 0:
            if (answer[turn][1] - answer[turn][0]) > ((i - j) - j):
                answer[turn][1] = i-j
                answer[turn][0] = j
            
    turn += 1

for i in answer:
    for j in i :
        print(j, end=' ')
    print()
