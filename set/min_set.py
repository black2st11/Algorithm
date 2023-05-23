import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().rstrip().split())

numbers = Counter()

for _ in range(2):
    for i in list(map(int, sys.stdin.readline().rstrip().split())):
        numbers[i] += 1

result = 0

for k, v in numbers.items():
    if v == 1:
        result += 1

print(result)
