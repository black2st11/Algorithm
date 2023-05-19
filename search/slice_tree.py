"""
https://www.acmicpc.net/problem/2805

result 부분에서 시간초과가 걸려서 람다로 바꿈

"""
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

trees = list(map(int, sys.stdin.readline().rstrip().split()))

lt = 0
rt = max(trees)

while lt <= rt:
    mid = (lt + rt) // 2
    result = 0
    result = sum(map(lambda x: x - mid if x - mid > 0 else 0, trees))
    # 시간 초과 나옴
    # for tree in trees:
    #     if tree - mid > 0:
    #         result += tree - mid

    if result >= k:
        lt = mid + 1
    else:
        rt = mid - 1

print(rt)
