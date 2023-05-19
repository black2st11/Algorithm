import sys


def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    array = array[1:]
    result = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            result += GCD(array[i], array[j])
    print(result)
