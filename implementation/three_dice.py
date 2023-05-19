import sys
from collections import Counter


def triple_dice(x):
    return 10000 + x * 1000


def twice_dice(x):
    return 1000 + x * 100


def single_dice(x):
    return x * 100


calcs = [single_dice, twice_dice, triple_dice]

dices = Counter()

dice_array = map(int, sys.stdin.readline().rstrip().split())

for dice in dice_array:
    dices[dice] += 1

dices = sorted(dices.items(), key=lambda item: item[0], reverse=True)
result = max(dices, key=lambda item: item[1])

print(calcs[result[1] - 1](result[0]))
