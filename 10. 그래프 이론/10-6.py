import sys
input = sys.stdin.readline
from collections import deque

# 노드의 갯수 V와 간선의 갯수 E
v, e = map(int, input().split())
# 간선의 정보를 저장할 graph 선언
graph = [[] for _ in range(v+1)]
# 각 노드의 진입차수를 indegree에 저장
indegree = [0] * (v+1)

# 각 간선의 정보 받아오기
for _ in range(e):
    # 위상 정렬에서 간선은 단방향
    start, end = map(int, input().split())
    # 간선의 정보와 진입차수 업데이트
    graph[start].append(end)
    indegree[end] += 1

# 위상정렬 함수
def topology_sort():
    # 지나간 노드를 순차적으로 저장할 result 선언
    result = []
    # 위상정렬은 queue를 사용
    q = deque()
    # 진입차수가 0인 노드부터 시작
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        # queue에서 노드를 하나 꺼냄
        now = q.popleft()
        # 꺼낸 노드를 result에 저장
        result.append(now)
        for next in graph[now]:
            # 꺼낸 노드와 연결된 노드의 진입차수 1씩 감소
            indegree[next] -= 1
            # 진입차수가 0인 노드를 queue에 추가
            if indegree[next] == 0:
                q.append(next)
    # 노드들의 순서 출력
    for r in result:
        print(r, end=" ")

topology_sort()
