n = int(input())
store = list(map(int, input().split()))
# max_food는 1번째부터 n-1번째 창고까지를 약탈했을 때 최대로 얻을 수 있는 식량의 양이다
max_food = [0]*(n+1)
# n = 1일 때는 첫 창고에 있는 식량이 최댓값
max_food[1] = store[0]
# n = 2일 때는 첫 창고와 두 번째 창고중에 더 큰 창고를 털었을 때 최대값을 가진다
max_food[2] = max(store[0],store[1])
for i in range(3, n+1):
    # f(n) = max(f(n-1), f(n-2)+n번째 식량창고에 들어있는 식량의 양)
    max_food[i] = max(max_food[i-1], max_food[i-2]+store[i-1])
print(max_food[n])