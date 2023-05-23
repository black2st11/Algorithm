import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

origin_set = set()
compare_list = []
result = 0

for _ in range(n):
    origin_set.add(sys.stdin.readline().rstrip())

for _ in range(m):
    if sys.stdin.readline().rstrip() in origin_set:
        result += 1

print(result)
