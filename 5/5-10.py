def dfs(x,y):
    if x not in range(m) or y not in range(n):
        return 0
    elif graph[y][x] == 1:
        return 0
    else:
        graph[y][x] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return 1

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += dfs(j, i)
print(result)