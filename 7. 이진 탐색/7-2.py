# 이진 탐색
def binary_search(array, target, begin, end):
    # target이 array에 없는 경우 None 반환
    if begin > end: return None
    mid = (begin + end) // 2
    # 중간점이 target인 경우 mid 반환
    if array[mid] == target:
        return mid
    # 중간값보다 target이 작은 경우 왼쪽 절반 탐색
    elif array[mid] > target:
        return binary_search(array, target, begin, mid-1)
    # target이 중간값보다 큰 경우 오른쪽 절반 탐색
    else:
        return binary_search(array, target, mid+1, end)

# n은 array의 크기, target은 찾는 값
n, target = list(map(int, input().split()))
# array의 값 받아오기
array = list(map(int, input().split()))

# target의 위치 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
