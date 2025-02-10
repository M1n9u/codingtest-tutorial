import sys
input = sys.stdin.readline
INF = int(1e9)
import heapq

# 도시의 갯수 N, 통로의 갯수 M, 메시지를 보내고자 하는 도시 C를 입력받음
n, m, c = map(int, input().split())
# 도시의 갯수가 많고 시작 도시가 정해져 있으므로 다익스트라 알고리즘 사용
graph = [[] for _ in range(n+1)]
# 통로의 정보를 입력받아 graph에 저장
for _ in range(m):
    start, dest, time = map(int, input().split())
    graph[start].append((dest, time))

# C에서 각 도시로 메시지를 보내는데 필요한 시간을 INF로 초기화
result = [INF] * (n+1)
# 다익스트라 알고리즘을 수행할 heapq 선언
queue = []
# 다익스트라 알고리즘
def dikstra(start):
    result[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        t, now = heapq.heappop(queue)
        if result[now] < t:
            continue
        for (next, t_next) in graph[now]:
            cost = t + t_next
            if result[next] > cost:
                result[next] = cost
                heapq.heappush(queue, (cost, next))

dikstra(c)
# count는 신호를 보낼 수 있는 도시의 갯수
count = 0
# 동시에 신호를 보내므로 신호를 보내는데 필요한 시간은 result의 최댓값
max_time = 0
for i in range(1,n+1):
    if result[i] != INF:
        count += 1
        max_time = max(max_time, result[i])
# 시작 노드 c를 제외한 나머지 도시의 갯수와 시간 출력
print(count - 1, end=" ")
print(max_time)