import sys
INF = int(1e9)

# 노드 개수와 간선 개수 입력
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

# 그래프들의 거리는 처음에는 크게 설정
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신은 0으로 설정
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 그래프 생성
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = c

# a와 b 간의 거리와 중간 노드를 거쳐가는 부분을 고려
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])

# 조회시에는 이중 배열이기에 이중 반복문
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY")
        else :
            print(graph[a][b], end=' ')
    print( )