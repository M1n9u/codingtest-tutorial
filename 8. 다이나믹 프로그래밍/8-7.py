# 2X1, 1X2, 2X2의 3가지 덮개로 2XN의 바닥을 채울 수 있는 경우의 수를 구하는 프로그램
# 바닥의 길이를 받아오기
n = int(input())
# result는 각 길이의 바닥을 채울 경우의 수 저장
result = [0]*(n+1)
# N = 1일 경우에는 2X1로만 채울 수 있음
result[1] = 1
# N = 2일 경우에는 2X1 두개, 1X2 두개, 2X2 한개로 총 3개의 경우의 수
result[2] = 3
# N >= 3일 경우에는 마지막을 2X1하나로 채우거나 2X2 하나 혹은 1X2 두개로 채우는 경우의 수를 더함
for i in range(3,n+1):
    result[i] = (result[i-1] + 2 * result[i-2]) % 796796
print(result[n])