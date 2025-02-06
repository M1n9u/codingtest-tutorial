# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 각 위치부터 배열의 끝까지 중 최솟값을 찾아 현재 위치와 변환
for i in range(len(array)):
    min_pos = i
    # 현재 위치부터 배열의 끝까지 탐색
    for j in range(i,len(array)):
        # 최솟값의 위치를 min_pos로 저장
        if array[min_pos]>array[j]:
            min_pos = j
    # 현재 위치의 값이 최솟값이면 넘어가기
    if i==min_pos: continue
    # 현재 위치의 값과 최솟값의 위치 바꾸기
    array[i], array[min_pos] = array[min_pos], array[i]

print(array)