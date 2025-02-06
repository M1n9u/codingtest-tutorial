# 퀵 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    # 배열의 원소가 하나 이하라면 정렬하지 않음
    if len(arr) <= 1:
        return arr
    # 첫 원소를 pivot으로 선택
    pivot = arr[0]
    # pivot을 제외한 나머지 원소들을 tail로 설정
    tail = arr[1:]
    # pivot보다 작은 원소를 left, pivot보다 큰 원소를 right로 분할
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    # left와 right에 재귀함수로 정렬을 진행한 후 pivot과 합쳐 정렬 완료
    return quick_sort(left)+[pivot]+quick_sort(right)

array = quick_sort(array)
print(array)