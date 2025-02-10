import sys
input = sys.stdin.readline
INF = int(1e9)

# 회사의 수 N과 도로의 수 M을 받아오기
n, m = map(int, input().split())
# 회사의 수와 도로의 수가 적으므로 플로이드 워셜 알고리즘 사용
graph = [[INF]*(n+1) for _ in range(n+1)]
# 같은 위치로 이동하는 비용은 0으로 초기화
for i in range(n):
    graph[i][i] = 0
for _ in range(m):
    # 도로는 양방향이므로 도로가 있는 회사 사이의 거리를 1로 설정
    start, dest = map(int, input().split())
    graph[start][dest] = 1
    graph[dest][start] = 1

# 도착지 x와 소개팅 장소 k 받아오기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: continue
        for k in range(1,n+1):
            if i==k or j==k: continue
            graph[j][k] = min(graph[j][i]+graph[i][k], graph[j][k])

# 1번 회사에서 K번 회사를 지나 X로 가는 시간 출력
time = graph[1][k] + graph[k][x]
if time >= INF:
    print(-1)
else:
    print(time)