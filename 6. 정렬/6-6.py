# 계수 정렬
# 리스트의 최댓값과 최솟값의 차이가 크지 않고 모든 원소가 양의 정수일 때만 사용 가능
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 0부터 최댓값까지 각 숫자가 몇번 들어가는지 카운팅
num_data = [0]*(max(array)+1)
for data in array:
    num_data[data] += 1

# 각 원소들을 해당 갯수만큼 갖는 새로운 배열을 정렬된 배열로 출력
sorted_array = sum([[x]*num_data[x] for x in range(len(num_data))], [])
print(sorted_array)