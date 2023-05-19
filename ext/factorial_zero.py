"""
https://www.acmicpc.net/problem/1676
문제를 잘 못 이해함
N! 라고 하길래
5
120, 24, 6, 2, 1
로 생각해서 0이 안나오는 구간까지의 인덱스를 구하는 줄 알았음.
하지만 아니네
"""
import sys

array = [0] * 501

array[0] = 1
array[1] = 1

for i in range(2, 501):
    array[i] = i * array[i - 1]


n = int(sys.stdin.readline().rstrip())

count = 0
temp = array[n]
while True:
    if temp % 10 == 0:
        temp //= 10
        count += 1
    else:
        break

print(count)
