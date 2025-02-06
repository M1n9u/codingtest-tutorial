# n은 입력받을 숫자의 갯수
n = int(input())
# n개의 숫자를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 리스트를 내림차순으로 정렬
array = sorted(array)
# 리스트의 각 원소를 공백으로 구분하여 출력
for i in array:
    print(i, end=' ')