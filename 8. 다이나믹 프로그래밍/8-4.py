# 보텀업 프로그래밍
def fibo(n):
    # f(1)과 f(2)를 사용하여 n까지 순차적으로 피보나치 수열 계산
    fib = [0]*100
    fib[1] = 1
    fib[2] = 1
    for i in range(3,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

print(fibo(99))