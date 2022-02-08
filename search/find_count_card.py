"""
https://www.acmicpc.net/problem/10816

처음에 카운터를 사용했는데 문제는 이분탐색 이후에 있는지 확인하고 카운터를 써서 오히려 시간초과나버림
그냥 카운터 썼으면 안나왔을텐데
"""
import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())

origin_card = list(map(int, sys.stdin.readline().rstrip().split()))

# origin_card.sort()

m = int(sys.stdin.readline().rstrip())

compare_card = list(map(int, sys.stdin.readline().rstrip().split()))

counter = Counter(origin_card)

print(" ".join(f"{counter[c]}" if c in counter else "0" for c in compare_card))

for i in range(len(compare_card)):
    comp = compare_card[i]
    lt = 0
    rt = len(origin_card) - 1
    while lt <= rt:
        mid = (lt + rt) // 2

        if comp > origin_card[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    else:
        if lt >= len(origin_card):
            print(0, end=" ")
            continue
        if comp == origin_card[lt]:
            cnt = 0
            while origin_card[lt] == comp:
                cnt += 1
                lt += 1
                if lt >= len(origin_card):
                    break

            print(cnt, end=" ")
        else:
            print("0", end=" ")
