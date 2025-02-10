# 간단한 다익스트라 알고리즘
import sys
input = sys.stdin.readline
# 초기화 값으로 1e9 채택
INF = int(1e9)

# N은 노드의 갯수, M은 간선의 갯수
n, m = list(map(int, input().split()))
# 시작 노드를 받아오기
start = int(input())
# 각 노드의 간선과 거리를 받을 graph, visited 선언
# 노드 번호와 인덱스가 일치하게 하기 위해 n+1 길이의 리스트 생성
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
# distance는 start로부터 해당 노드까지의 거리를 저장
distance = [INF] * (n+1)

# M개의 간선정보를 입력받음
for i in range(m):
    # node는 간선의 시작노드, dest는 간선의 목적지, dist는 간선의 거리이다
    node, dest, dist = list(map(int, input().split()))
    graph[node].append((dest, dist))

# 방문하지 않은 노드들 중에서 start와의 거리가 가장 짧은 노드를 불러온다
def get_smallest_node():
    min_dist = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_dist and not visited[i]:
            index = i
            min_dist = distance[i]
    return index


def dijkstra(start):
    # 시작 노드로부터 시작 노드까지의 거리는 0
    distance[start] = 0
    # 시작 노드에 연결된 각 노드의 거리를 간선의 길이로 초기화
    for (node, dist) in graph[start]:
        distance[node] = dist
    # n-1번 반복복
    for _ in range(n-1):
        # 가장 짧은 거리의 노드 선택 후 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 해당 노드에 연결된 노드들의 distance 값을 거리+간선의 길이와 원래의 distance 값 중
        # 짧은 값으로 저장
        for (node, dist) in graph[now]:
            distance[node] = min(distance[now]+dist, distance[node])

dijkstra(start)
for i in range(1, n+1):
    # start 노드에서 해당 노드에 갈 수 없을 경우 INFINITY 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])