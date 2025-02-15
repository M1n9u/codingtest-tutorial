import sys
input = sys.stdin.readline
# 팀 결성 문제는 서로소 집합 알고리즘 사용
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

# N+1개의 학생들이 있고 M개의 연산 수행
n, m = map(int, input().split())
# 0에서 N까지 번호가 부여되므로 range(n+1)로 초기화
parent = list(range(n+1))
# 출력할 내용을 저장할 result
result = []
# M개의 연산 수행
for _ in range(m):
    operation, a, b = map(int, input().split())
    # 앞의 숫자가 0이면 팀을 합칠 union 연산 수행
    if operation == 0:
        union_parent(parent, a, b)
    # 앞의 숫자가 1이면 a와 b가 같은 팀에 있는지 확인함
    else:
        # 같은 팀에 있다면 YES 출력
        if find_parent(parent, a) == find_parent(parent, b):
            result.append("YES")
        # 다른 팀이라면 NO 출력
        else:
            result.append("NO")

# 결과 출력
for res in result:
    print(res)