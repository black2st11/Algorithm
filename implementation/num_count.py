import sys
from collections import Counter


n = sys.stdin.readline().rstrip()
counter = Counter()

for i in list(map(int, sys.stdin.readline().rstrip().split())):
    counter[i] += 1

print(counter[int(sys.stdin.readline().rstrip())])
