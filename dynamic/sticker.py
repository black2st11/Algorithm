"""
백준 9465
"""

import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    card_len = int(sys.stdin.readline().rstrip())

    array_top = list(map(int, sys.stdin.readline().rstrip().split()))
    array_bottom = list(map(int, sys.stdin.readline().rstrip().split()))

    if card_len == 1:
        print(max(array_top, array_bottom)[0])
        continue
    dp_top = [0] * (len(array_top) + 1)
    dp_bottom = [0] * (len(array_bottom) + 1)

    dp_top[1] = array_top[0]
    dp_bottom[1] = array_bottom[0]

    dp_top[2] = dp_bottom[1] + array_top[1]
    dp_bottom[2] = dp_top[1] + array_bottom[1]

    for i in range(3, len(array_top) + 1):
        dp_top[i] = max(
            dp_bottom[i - 1] + array_top[i - 1], dp_bottom[i - 2] + array_top[i - 1]
        )
        dp_bottom[i] = max(
            dp_top[i - 1] + array_bottom[i - 1], dp_top[i - 2] + array_bottom[i - 1]
        )

    top_max = max(dp_top)
    bottom_max = max(dp_bottom)
    print(max(top_max, bottom_max))
