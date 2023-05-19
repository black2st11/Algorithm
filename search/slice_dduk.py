import sys

n , m = map(int, sys.stdin.readline().rstrip().split())

array = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(array, m):
    start = 0
    end = max(array)


    while start <= end :
        total = 0
        mid = (start+end) // 2

        for i in array:
            if i > mid :
                total += i - mid
        
        if total > m :
            start = mid + 1
        elif total <= m :
            end = mid - 1
    
    print(mid)

binary_search(array, m)