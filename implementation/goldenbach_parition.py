import sys

T = int(sys.stdin.readline().rstrip())

numbers = [0 for i in range(1000000)]

for i in range(2, 500000):
    if numbers[i] == 0:
        for j in range(2 * i, 1000000, i):
            numbers[j] = 1

for _ in range(T):
    result = 0
    N = int(sys.stdin.readline().rstrip())
    for j in range(2, int(N / 2) + 1):
        if numbers[j] == 0 and numbers[N - j] == 0:
            result += 1
    else:
        print(result)
