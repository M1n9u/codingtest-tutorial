import sys
input = sys.stdin.readline

# 부모 노드를 찾기
def find_parent(parent, x):
    # 부모 노드가 자신이 아니면 재귀적으로 부모 노드를 찾으며 경로 압축
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 집합을 합치기
def union_parent(parent, a, b):
    # 합칠 집합의 부모 노드 가져오기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 더 높은 부모 노드의 부모 노드를 낮은 부모 노드로 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# V는 노드의 갯수, E는 union연산의 갯수
v, e = map(int, input().split())
# 각 노드의 부모 노드를 자신으로 초기화
parent = list(range(v+1))

# E번의 union 연산 수행
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a,b)

# 각 원소의 부모 노드 출력
print("각 원소가 속한 집합: ", end="")
for p in parent[1:]:
    print(find_parent(parent, p), end=" ")


