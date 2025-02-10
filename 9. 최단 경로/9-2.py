import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# N은 노드의 갯수, M은 간선의 갯수
n, m = list(map(int, input().split()))
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
# 시작 노드 번호 입력받기
start = int(input())

# 각 간선 정보 입력받기
for _ in range(m):
    node, dest, dist = list(map(int, input().split()))
    graph[node].append((dest, dist))

# 개선된 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드의 거리를 0으로 설정하고 heapq에 시작 노드를 넣음
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    # heapq가 빌 때까지 반복
    while q:
        # heapq의 노드들 중 거리가 가장 짧은 노드를 꺼냄
        (d_now, now) = heapq.heappop(q)
        # 이미 처리된 노드인 경우 건너뜀
        if distance[now] < d_now:
            continue
        # 꺼낸 노드의 인접 노드들을 확인
        for (next, d) in graph[now]:
            # 꺼낸 노드의 거리 + 간선의 길이가 인접 노드의 거리보다 짧다면 해당 노드의 distance 값 수정
            cost = d_now + d
            if distance[next] > cost:
                distance[next] = cost
                # 수정한 노드와 거리를 heapq에 추가
                heapq.heappush(q, (cost, next))
        
dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])