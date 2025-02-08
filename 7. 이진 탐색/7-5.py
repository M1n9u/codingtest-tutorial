import sys

# 전자 매장에 N개의 부품 존재
n = int(input())
# 버퍼로 전자 매장에 존재하는 모든 부품 받아오기
buff = sys.stdin.readline().rstrip()
comp = list(map(int, buff.split()))

# 손님이 M개의 부품 요청
m = int(input())
# 버퍼로 손님이 요청한 M개의 부품 받아오기
buff = sys.stdin.readline().rstrip()
request = list(map(int, buff.split()))

# 매장 부품에 요청한 부품이 있는지 찾기 위한 이진 탐색 알고리즘
def binary_search(array, target, begin, end):
    if begin > end:
        return None
    mid = (begin + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, begin, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

# 이진 탐색을 위해 부품 리스트를 정렬
comp.sort()
for req in request:
    result = binary_search(comp, req, 0, n-1)
    # 부품이 없는 경우 no 출력
    if result == None:
        print("no", end=" ")
    # 부품이 있는 경우 yes 출력
    else:
        print("yes", end=" ")