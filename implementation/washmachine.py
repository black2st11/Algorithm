import sys

T = int(sys.stdin.readline().rstrip())
coins = [25, 10, 5, 1]


def calc_coin(money, coin):
    if money <= 0:
        return [0, 0]

    return [money // coin, money % coin]


for _ in range(T):
    result = []
    C = int(sys.stdin.readline().rstrip())

    for coin in coins:
        count, money = calc_coin(C, coin)
        result.append(count)
        C = money

    print(*result, sep=" ")
