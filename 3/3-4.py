# 자연수 n, k값 가져오기
n, k = map(int,input().split())
result = 0

while n != 1:
    # n이 k의 배수이면 n을 k로 나눈다
    if n % k == 0:
        n = n // k
        result += 1
    # n이 k의 배수가 아니면 n이 k의 배수가 될 때까지 1씩 뺀다
    else:
        if(n % k != n):
            result += n % k
            n -= (n % k)
        else:
            result += n - 1
            n = 1
# n이 1이 될 때까지의 연산 횟수를 출력       
print(result)