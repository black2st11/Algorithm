'''
거스름돈으로 사용하는 동전은 500원, 100원, 50원, 10원 이다.
거스름돈으로 주는 최소의 동전 개수를 구해라
'''
import random

remain = random.randrange(1000, 5000, 10)

coins = [500, 100, 50, 10]
count = 0

for coin in coins:
    count +=  remain // coin
    remain %= coin
print(count)
