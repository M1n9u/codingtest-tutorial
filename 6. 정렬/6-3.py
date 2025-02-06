# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 두 번째 원소부터 실행
for i in range (1,len(array)):
    # 앞으로 한칸씩 이동하면서 비교
    for j in range(i,0,-1):
        # 현재 위치의 데이터보다 앞의 데이터가 크다면 서로 위치를 바꿈
        if array[j]<array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        # 앞의 데이터가 더 작다면 그 위치에서 멈춤
        else:
            break

print(array)