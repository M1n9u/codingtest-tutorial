# N은 가진 화폐의 종류 수, M은 만들어야 하는 금액
n, m = list(map(int, input().split()))
# N종류의 화폐가 가진 가치를 입력으로 받아옴
coins = [0]*n
for i in range(n):
    coins[i] = int(input())

# 화폐 가치가 10000까지이므로 10001은 가진 화폐들의 조합으로 만들 수 없음을 의미
result = [10001]*(m+1)
# 가진 화폐의 가치와 같은 금액은 1개의 화폐만 가지고 만들 수 있으므로 1값을 가짐
for coin in coins:
    # 화폐의 가치가 만들어야 하는 금액보다 클 경우는 고려하지 않음
    if(coin > m):
        break
    result[coin] = 1

for i in range(1,m+1):
    for coin in coins:
        # 금액에서 각 화폐의 가치만큼 뺀 금액의 result 값 + 1이 현재 값보다 작을 경우 저장
        if i - coin > 0:
            result[i] = min(result[i], result[i-coin]+1, 10001)
# M원을 만들지 못하는 경우 -1 출력
if(result[m] > 10000):
    print(-1)
else:
    print(result[m])