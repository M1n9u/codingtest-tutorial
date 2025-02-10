# 플로이드 워셜 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 갯수 N과 간선의 갯수 M을 받아오기
n = int(input())
m = int(input())

# 각 노드에서 다른 노드까지의 최소 거리를 값으로 가지는 2차원 그래프
# 초기값은 INF로 설정정
graph = [[INF]*(n+1) for _ in range(n+1)]
# 같은 노드끼리 이동하는 비용은 0으로 설정
for i in range(1,n+1):
    graph[i][i] = 0

# 각 간선 정보를 받아오기
for _ in range(m):
    node, dest, dist = map(int, input().split())
    # 간선이 있는 노드의 비용을 받아온 비용으로 초기화
    graph[node][dest] = dist

# 각 노드에 대해 플로이드 워셜 알고리즘 수행
# j 노드에서 i 노드를 지나 k 노드로 가는 경로에 대해 테이블 업데이트
for i in range(1,n+1):
    for j in range(1,n+1):
        # i, j, k중 같은 노드가 존재하면 건너뛰기
        if i == j: continue
        for k in range(1,n+1):
            if i == k or j == k: continue
            # j 노드에서 i 노드를 지나 k 노드로 가는 비용이 원래의 j에서 k로 가는 비용보다 작을 경우 변경
            graph[j][k] = min(graph[j][i]+graph[i][k], graph[j][k])

# 2차원 그래프 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()