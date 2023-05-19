import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
t = int(sys.stdin.readline().rstrip())

m += t

head = m // 60
n += head
m -= head * 60

print(n % 24, m, sep=" ")
