import sys

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (
            numbers[0] * i + numbers[1] * j == numbers[2]
            and numbers[3] * i + numbers[4] * j == numbers[5]
        ):
            print(i, j)
