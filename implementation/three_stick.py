import sys

sticks = list(map(int, sys.stdin.readline().rstrip().split()))

sticks.sort()

if sticks[2] >= sticks[0] + sticks[1]:
    print((sticks[0] + sticks[1]) * 2 - 1)
else:
    print(sum(sticks))
