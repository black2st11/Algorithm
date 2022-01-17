import sys

t = int(sys.stdin.readline().rstrip())

array = [0] * 10001

for i in range(t):
    array[int(sys.stdin.readline().rstrip())] += 1

for i in range(len(array)):
    for _ in range(array[i]):
        print(i)