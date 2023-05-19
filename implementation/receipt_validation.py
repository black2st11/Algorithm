import sys

result = 0

estimation = int(sys.stdin.readline().rstrip())
count = int(sys.stdin.readline().rstrip())

for i in range(count):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    result += n * m

print("Yes" if result == estimation else "No")
