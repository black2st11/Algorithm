import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list(sys.stdin.readline().rstrip().split())

arr.sort()
nec = ["a", "e", "i", "o", "u"]


def pick(item, idx):
    if len(item) == n:
        flag = 0
        for i in range(len(nec)):
            if nec[i] in item:
                flag += 1

        if flag >= 1 and n - flag >= 2:
            print("".join(item))
        return

    for i in range(idx, len(arr)):
        item.append(arr[i])
        pick(item, i + 1)
        item.pop()


pick([], 0)
