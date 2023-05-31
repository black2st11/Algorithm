import sys


def divide(arr):
    length = len(arr)
    if length != 1:
        return (
            divide(arr[0 : length // 3])
            + " " * (length // 3)
            + divide(arr[length // 3 * 2 :])
        )
    else:
        return arr


while True:
    try:
        N = int(sys.stdin.readline().rstrip())

        initial_dash = "-" * 3**N

        print(divide(initial_dash))
    except (EOFError, ValueError):
        break
