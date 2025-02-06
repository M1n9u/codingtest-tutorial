# 여행가 A가 N*N의 정사각형 공간 위에 있다
n = int(input())
# 여행자 A가 이동할 방향을 받아온다
move = input().split()
# L은 왼쪽, R은 오른쪽, U는 위, D는 아래로 이동
action = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
# 시작 지점은 (1,1)로 고정정
x, y = 1, 1
for actions in move:
    nx = x + action[actions][0]
    ny = y + action[actions][1]
    # 이동 후 정사각형 공간을 벗어난다면 이동이 무시된다
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
# 모든 이동이 수행된 후 마지막 여행자의 위치를 출력
print(x, y)