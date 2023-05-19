import sys

counter = {i: 0 for i in range(1, 31)}

for _ in range(28):
    n = int(sys.stdin.readline().rstrip())
    counter[n] += 1

for k, v in counter.items():
    if v == 0:
        print(k)
