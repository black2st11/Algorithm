import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

numbers.sort(reverse=True)

print(numbers[m - 1])
