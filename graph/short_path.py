import heapq
import sys

# 노드 개수와 간선의 개수를 입력받는다.
n, m = map(int, sys.stdin.readline().rstrip().split())

# 시작점을 설정한다
start = int(sys.stdin.readline().rstrip())

# 0은 제외 노드 개수 만큼 설정
graph = [[] for _ in range(n + 1)]

# 노드간의 거리를 크게 설정
distance = [999999] * (n + 1)
# 시작점과의 거리는 0으로 설정
distance[start] = 0

# 그래프 생성
for i in range(m):
    # a 출발 노드, b 목표 노드, c 거리
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

q = []

# 간선의 가중치가 짧은 순으로 뽑기위해 우선순위 큐 설정
heapq.heappush(q, (0, start))

while q:
    item = heapq.heappop(q)
    # 현재 거리 배열에 들어가 있는 값과 그래프에 들어가 있는 가중치 값 비교
    if distance[item[1]] < item[0]:
        continue

    # 빼낸 노드에서 연결된 노드 비교
    for node in graph[item[1]]:
        if distance[node[0]] > node[1] + distance[item[1]]:
            distance[node[0]] = node[1] + distance[item[1]]
            heapq.heappush(q, (distance[node[0]], node[0]))

# 연결된 부분은 최단 거리 표현, 안된 경우 -1
for i in range(1, n + 1):
    a = 'INF' if distance[i] == 999999 else distance[i]
    print(a)
