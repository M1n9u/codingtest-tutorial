# 탑다운 프로그래밍
# 이미 계산한 피보나치 수열 값을 계산할 fib 배열 선언
fib = [0]*100
# f(1)=f(2)=1
fib[1] = 1
fib[2] = 1
def fibo(n):
    # 피보나치 수열 값이 이미 계산한 수라면 그 수 반환
    if (fib[n] != 0):
        return fib[n]
    # 계산되지 않았을 경우에만 재귀함수를 사용해 새로 계산
    else:
        fib[n] = fibo(n-2) + fibo(n-1)
        return fib[n]

print(fibo(99))