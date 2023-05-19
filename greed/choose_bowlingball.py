import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

balls = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0

for i in range(len(balls)-1):
    for j in range(i+1, len(balls)):
        if balls[i] != balls[j]:
            count += 1

print(count)