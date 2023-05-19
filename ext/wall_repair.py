# 푸는 중
import sys

n = int(sys.stdin.readline().rstrip())

weak = list(map(int, sys.stdin.readline().rstrip().split()))

dist = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(len(weak)):
    for j in range(i + 1, len(weak)):
        pass
