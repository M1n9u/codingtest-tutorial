import sys
input = sys.stdin.readline
from collections import deque
import copy

# 커리큘럼은 위상 정렬 알고리즘 이용
# N은 강의의 갯수
n = int(input())
graph = [[] for _ in range(n+1)]
# 위상 정렬을 사용하기 위해 진입차수 변수 생성
indegree = [0] * (n+1)
# 각 강의를 듣기 위해 필요한 시간을 저장할 time 선언
time = [0] * (n+1)

for i in range(1,n+1):
    # buffer에 해당 강의의 강의시간, 선수과목을 받아옴. 버퍼의 마지막에는 -1값이 들어옴
    buf = list(map(int, input().split()))
    # time에 강의시간 저장
    time[i] = buf[0]
    # 강의시간과 마지막 -1을 제외한 나머지 선수과목들을 그래프에 저장하고 진입차수 수정
    for num in buf[1:-1]:
        graph[num].append(i)
        indegree[i] += 1

# 위상정렬
def topology_sort():
    # time 변수를 수정하지 않고 result에 time값을 그대로 복사해 저장
    # result는 각 강의를 수강하기 위해 필요한 최소 시간을 계산해서 저장
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for next in graph[now]:
            # result에 선수과목을 듣는 시간을 더함
            result[next] = max(result[next],result[now]+time[next])
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    # 최소 시간 출력
    for res in result[1:]:
        print(res)

topology_sort()