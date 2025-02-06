# N*M크기의 미로 받아오기
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))
# 처음 위치는 (1,1)로 고정
# 미로는 (0,0)부터 (N-1,M-1)까지 값을 가지고, 괴물이 있는 위치는 0, 없는 위치는 1로 표기
x, y = 1, 1
# 미로를 탐색하기 위해 bfs 알고리즘 사용
def bfs(x,y):
    from collections import deque
    queue = deque()
    # 초기 위치를 queue에 넣음
    queue.append((x,y))
    # queue가 빌 때까지 실행
    while queue:
        # 오른쪽 아래 끝에 도달했을 경우 미로를 빠져나와 실행 종료
        if y==n and x==m: break
        x,y = queue.popleft()
        # 상하좌우의 위치가 인접 노드
        next_nodes = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        for next_node in next_nodes:
            nx, ny = next_node
            # 미로를 벗어나지 않고 괴물이 없는 칸인 경우 queue에 추가
            if ny in range(1,n+1) and nx in range(1,m+1) and maze[ny-1][nx-1] == 1:
                queue.append((nx,ny))
                # 해당 칸까지의 이동 횟수를 저장
                maze[ny-1][nx-1] = maze[y-1][x-1] + 1
bfs(x,y)
# 마지막 칸까지 최단 거리를 출력
print(maze[-1][-1])