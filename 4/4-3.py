pos = input()
row = int(pos[1])
col = int(ord(pos[0]))-int(ord('a'))+1
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
result = 0
for step in steps:
    nr,nc = row+step[0], col+step[1]
    if nr in range(1,9) and nc in range(1,9):
        result += 1
print(result)