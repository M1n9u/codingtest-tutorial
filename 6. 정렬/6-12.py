# n은 a, b 배열의 크기, k는 최대 바꿔치기 연산의 횟수
n, k = map(int, input().split())
# 크기가 n인 배열을 2개 받아와 각각 a와 b에 저장
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# a는 내림차순, b는 오름차순으로 정렬한다
a.sort()
b.sort(reverse=True)
for i in range(k):
    # a의 최솟값부터 b의 최댓값과 비교하여 바꾼다
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    # a의 원소보다 b의 원소가 작으면 반복문을 나간다
    else:
        break
# 최대 k번 바꿔치기 연산을 수행한 후의 a배열의 합의 최댓값 출력
print(sum(a))