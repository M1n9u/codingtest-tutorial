n, m = map(int,input().split())
y, x, direction = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
# 0: 북, 1: 동, 2: 남, 3: 서
move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# 첫 칸을 방문한 것으로 처리
result = 1
# 움직임이 끝나는 경우 False로 변경
cond = True
# 방문한 칸을 2로 표시
board[y][x] = 2
while cond:
    # 현재 방향을 기준으로 왼쪽 방향부터 탐색
    for i in range(1,5):
        # 왼쪽으로 회전
        d = direction - i
        if d < 0: d += 4
        # 왼쪽 방향으로 이동
        nx, ny = x + move[d][0], y + move[d][1]
        # 이동한 칸이 0이라면 이동
        if board[ny][nx] == 0:
            board[ny][nx] = 2
            x, y = nx, ny
            result += 1
            # 방향 변경경
            direction = d
            break
        # 주변의 모든 칸이 방문했거나 바다일 경우 뒤로 이동
        if i == 4:
            nx, ny = x - move[direction][0], y - move[direction][1]
            # 뒷 칸이 바다라면 이동 종료료
            if board[ny][nx] == 1:
                cond = False
                break
            # 뒷 칸으로 이동
            else:
                x, y = nx, ny
                break
print(result)