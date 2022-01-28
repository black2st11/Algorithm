"""
https://www.acmicpc.net/problem/15686

1. 처음에는 거리의 누적 합으로 해서 접근을 했지만 TC는 통과, 
제출은 실패해서 누적 합으로 할 경우 애매한 경우가 있는 것을 발견하여
2. 완전 탐색으로 변경
"""

from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

# 집을 담을 집합
house = set()

# 치킨을 담을 집합
chicken = set()

# 리스트에서 치킨과 집에 대한 정보를 입력
for i in range(n):
    info = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(info)):
        if info[j] == 1:
            house.add((i + 1, j + 1))
        elif info[j] == 2:
            chicken.add((i + 1, j + 1))


result = []

# 누적합 방식
# 각각의 치킨 집이 모든 집에 대해 가지는 거리를 추산
for chick in chicken:
    c1, r1 = chick
    all_distance = 0
    for home in house:
        c2, r2 = home
        all_distance += abs(c1 - c2) + abs(r1 - r2)
    result.append([c1, r1, all_distance])


# 한 치킨이 가지는 모든 집에 대한 거리로 오름차순으로 정렬
result.sort(key=lambda x: (x[2]))

# 남기는 수 만큼 빼기 위해서 현재 치킨집의 수에서 남기는 m 만큼 빼면 몇 번 빼야하는 지 나옴
# 5개의 치킨집에서 3개를 남기려면 5 - 3 = 2 번을 빼야함
for _ in range(len(chicken) - m):
    result.pop()

answer = 0

# 이제는 집에서 제일 가까운 치킨 집의 거리를 구하고 그 거리를 한 곳에 더함
for home in house:
    c1, r1 = home
    min_distance = int(1e9)
    for item in result:
        c2, r2 = item[0], item[1]
        min_distance = min(abs(c1 - c2) + abs(r1 - r2), min_distance)
    answer += min_distance

print(answer)


# 조합

chicken_combination = list(combinations(chicken, m))

# 위의 거리 구하는 부분 함수화
def distance_min(chicken_combination):
    distance = 0
    for home in house:
        c1, r1 = home
        chicken_distance = int(1e9)
        for item in chicken_combination:
            c2, r2 = item[0], item[1]
            chicken_distance = min(abs(c1 - c2) + abs(r1 - r2), chicken_distance)
        distance += chicken_distance
    return distance


result = int(1e9)

for selected_chicken in chicken_combination:
    result = min(result, distance_min(selected_chicken))

print(result)
