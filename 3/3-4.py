n, k = map(int,input().split())
result = int(0)

while n != 1:
    if n % k == 0:
        n = n // k
        result += 1
    else:
        if(n % k != n):
            result += n % k
            n -= (n % k)
        else:
            result += n - 1
            n = 1
        
print(result)