# n, m, k를 공백으로 구분하여 입력받기
# n은 배열의 크기, m은 숫자가 더해지는 횟수, k는 연속해서 더할 수 있는 횟수
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# 입력받은 수 정렬하기
data.sort()
# 결과 값 초기화
result = 0

while True:
    # 가장 큰 수를 k번 더하기기
    for i in range(k):
        # m번 더해졌다면 반복문 탈출출
        if m == 0:
            break
        # 가장 큰 수를 결과 값에 더하기
        result += data[-1]
        # 더할 때마다 m 감소
        m -= 1
    # 두 번째로 큰 수를 한 번 더하기
    if m == 0:
        break
    result += data[-2]
    m -= 1

print(result)