from collections import deque

# 재귀함수를 사용하여 dfs 구현
def dfs(graph, node, visited):
    # 현재 노드를 방문 처리
    visited[node-1] = True
    print(node, end=' ')
    # 현재 노드의 인접 노드들을 가져옴
    next_nodes = graph[node-1]
    # 모든 방문하지 않은 노드들에 대해 dfs 실행
    for next_node in next_nodes:
        if not visited[next_node-1]:
            dfs(graph, next_node, visited)

# 재귀함수를 사용하지 않고 dfs 구현
def mydfs(graph, start, visited):
    # 첫 노드를 stack에 넣고 방문 처리
    stack = [start]
    visited[start-1] = True
    print(start, end=' ')
    # stack이 빌 때 까지 실행
    while stack:
        # start 노드를 stack의 마지막 노드로 설정
        start = stack[-1]
        # start 노드의 인접 노드들을 가져옴
        next_nodes = graph[start-1]
        for next_node in next_nodes:
            # 인접 노드들 중 방문하지 않은 노드가 있다면 stack에 해당 노드를 추가하고 방문 처리
            if not visited[next_node-1]:
                stack.append(next_node)
                visited[next_node-1] = True
                print(next_node, end=' ')
                break
            # 인접 노드들 중 방문하지 않은 노드가 없다면 stack에서 마지막 노드를 제거
            if next_node == next_nodes[-1]:
                stack.pop()



graph = [[2, 3, 8],[1, 7],[1, 4, 5],[3, 5],[3, 4],[7],[2, 6, 8],[1, 7]]
visited = [False]*8
mydfs(graph,1,visited)
print()
# bfs 구현
def bfs(graph, start, visited):
    # 첫 노드를 queue에 삽입하고 방문 처리
    queue = deque([start])
    visited[start-1] = True
    # queue가 빌 때 까지 실행
    while queue:
        # queue에서 첫 노드를 꺼냄
        next_node = queue.popleft()
        print(next_node,end=' ')
        # 가져온 노드의 인접한 노드중 방문하지 않은 노드들을 queue에 추가하고 방문 처리
        for node in graph[next_node-1]:
            if not visited[node-1]:
                visited[node-1] = True
                queue.append(node)

visited = [False]*8
bfs(graph,1,visited)