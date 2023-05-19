import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    
    for i in range((len(food_times))):
        heapq.heappush(q, (food_times[i], i+1))
        
    sum_value = 0
    previous_value = 0
    
    length = len(food_times)
    
    while sum_value + ((q[0][0] - previous_value) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous_value) * length
        length -= 1
        previous_value = now
    
    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]

n = list(map(int, input().split()))
m = int(input())
print(solution(n, m))