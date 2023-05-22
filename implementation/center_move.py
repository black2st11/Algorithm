import sys

N = int(sys.stdin.readline().rstrip())
duplicate_point = 3
point = 1


for i in range(1, N + 1):
    duplicate_point = (duplicate_point * 2) - 1
    result = point * 4 + duplicate_point
    point = result - duplicate_point
print(result)
