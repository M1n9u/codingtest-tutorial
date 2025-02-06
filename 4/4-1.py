n = int(input())
move = input().split()
action = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
x, y = 1, 1
for actions in move:
    nx = x + action[actions][0]
    ny = y + action[actions][1]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)