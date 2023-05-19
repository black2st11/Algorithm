"""
https://www.acmicpc.net/problem/10815
"""
import sys

n = int(sys.stdin.readline().rstrip())

origin_card = list(map(int, sys.stdin.readline().rstrip().split()))

origin_card.sort()
m = int(sys.stdin.readline().rstrip())

compare_card = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(len(compare_card)):
    comp = compare_card[i]
    lt = 0
    rt = len(origin_card) - 1
    while lt <= rt:
        mid = (lt + rt) // 2

        if comp == origin_card[mid]:
            print("1", end=" ")
            break
        elif comp >= origin_card[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    else:
        print("0", end=" ")
