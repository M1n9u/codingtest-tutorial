n = int(input())
result = 0
k, l = 3600, 1575
for i in range(n+1):
    if '3' in str(i):
        result += k
    else:
        result += l

print(result)