import sys
input = sys.stdin.readline

# 크루스칼 알고리즘을 사용하기 위한 경로 압축 서로소 집합 알고리즘
def find_parent(parent, x):
    if(parent[x] != x):
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

# 노드의 갯수 V와 간선의 갯수 E
v, e = map(int, input().split())
# 본인이 본인을 부모로 가지게 parent 초기화
parent = list(range(v+1))
# 간선의 정보를 담을 edge 선언
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 간선을 비용순으로 정렬하기 위해 cost를 앞으로 저장
    edges.append((cost, a, b))
# 비용순 정렬
edges.sort()

result = 0
for cost, a, b in edges:
    # 사이클이 포함되지 않으면 a와 b를 union하고 해당 간선을 신장 트리에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 신장 트리의 비용 출력
print(result)