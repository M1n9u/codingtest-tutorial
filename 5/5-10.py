# 상하좌우가 붙어있다고 가정할 때의 dfs 알고리즘
def dfs(x,y):
    # 틀 바깥인 경우는 제외
    if x not in range(m) or y not in range(n):
        return 0
    # 현재 위치가 칸막이인 경우 제외
    elif graph[y][x] == 1:
        return 0
    # 상하좌우의 위치에서 재귀함수로 dfs 알고리즘 구현
    else:
        # 방문한 위치는 1로 표기
        graph[y][x] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return 1
# N*M 크기의 얼음틀
n, m = map(int,input().split())
# 구멍이 뚫려있는 부분은 0, 칸막이가 있는 부분은 1로 표기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
result = 0
# 각 얼음틀 위치에서 dfs알고리즘을 수행하고, 수행할 때마다 1씩 더함
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += dfs(j, i)
# 얼음틀에서 만들어질 수 있는 얼음의 갯수 출력
print(result)