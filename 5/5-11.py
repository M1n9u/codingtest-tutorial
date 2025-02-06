
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

x, y = 1, 1
def bfs(x,y):
    from collections import deque
    queue = deque()
    queue.append((x,y))
    while queue:
        if y==n and x==m: break
        x,y = queue.popleft()
        next_nodes = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        for next_node in next_nodes:
            nx, ny = next_node
            if ny in range(1,n+1) and nx in range(1,m+1) and maze[ny-1][nx-1] == 1:
                queue.append((nx,ny))
                maze[ny-1][nx-1] = maze[y-1][x-1] + 1
bfs(x,y)
print(maze[-1][-1])