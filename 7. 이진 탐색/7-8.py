import sys

# N은 떡의 갯수, M은 손님이 요청한 떡의 길이
n, m = map(int, input().split())
# length에 각 N개의 떡의 길이를 각각 저장
buff = sys.stdin.readline().rstrip().split()
length = list(map(int, buff))
# 이진 탐색을 위해 length 정렬
length.sort()
# 절단기의 높이는 0에서 떡의 길이의 최댓값 사이로 설정한다
min_length, max_length = 0, length[n-1]
# 절단기의 높이를 0에서 떡의 길이의 최댓값 사이에서 이진 탐색
while (min_length <= max_length):
    # 최솟값과 최댓값의 절반 길이를 절단기의 높이로 설정
    mid = (min_length + max_length) // 2
    # total 손님이 받을 떡의 길이를 계산해서 저장
    total = 0
    for l in length:
        # 절단기의 높이보다 긴 떡의 경우에만 result에 더한다
        if (l > mid):
            total += (l - mid)
    # result가 손님이 요청한 떡의 길이와 같으면 탐색 종료
    if (total == m):
        break
    # 잘린 떡의 길이가 손님이 요청한 떡의 길이보다 짧으면 절단기의 높이를 낮춰야 하므로 절단기의 최댓값을 수정
    elif (total < m):
        max_length = mid - 1
    # 잘린 떡의 길이가 손님이 요청한 길이보다 길면 절단기의 높이를 높이기 위해 최솟값을 수정
    # 반복문이 끝났을 때 잘린 떡의 길이가 손님이 요청한 길이보다 길어야 하므로 result에 현재 절단기의 값 저장
    else:
        result = mid
        min_length = mid + 1

print(result)