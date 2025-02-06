# 체스판에서 나이트의 위치 받아오기
pos = input()
# a1, c3와 같이 열은 알파벳으로, 행은 숫자로 표기
row = int(pos[1])
col = int(ord(pos[0]))-int(ord('a'))+1
# 해당 위치에서 나이트가 갈 수 있는 모든 이동
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
result = 0
for step in steps:
    nr,nc = row+step[0], col+step[1]
    # 이동 시 체스판 안에 있다면 카운팅
    if nr in range(1,9) and nc in range(1,9):
        result += 1
# 한번 이동 시 나이트가 갈 수 있는 위치의 갯수 출력
print(result)