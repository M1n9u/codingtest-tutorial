import numpy as np

# N*M형태의 카드 배열을 받아와야 한다
n, m = map(int,input().split())
result = 0
for i in range(n):
    # 각 행의 카드 값 받아오기
    row = list(map(int, input().split()))
    # 각 행의 카드 중 최소값만을 선택하고 그 중 가장 큰 값을 result에 저장
    result = max(result, min(row))

print(result)