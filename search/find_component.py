import sys

n = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())

compare_array = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(array, element):
    temp = sorted(array)

    start = 0
    end = len(temp)

    while start <= end :
        mid = (start+end) // 2
        if temp[mid] > element :
            end = mid - 1
        elif temp[mid] < element :
            start = mid + 1
        elif temp[mid] == element :
            return print('yes')
    return print('no')

for i in compare_array:
    binary_search(array, i)


# 이게 더 파이썬스럽다.
for i in compare_array:
    if i in array:
        print('yes')
    else :
        print('no')