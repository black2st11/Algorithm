import sys

n = sys.stdin.readline().rstrip()

coins = list(map(int, sys.stdin.readline().rstrip().split()))

coins.sort()

answer = 1

for coin in coins:
    if answer < coin:
        break
    answer += coin

print(answer)
