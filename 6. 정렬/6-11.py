# 학생의 수 N을 입력받음
n = int(input())
# 학생의 이름과 성적을 info에 저장
info = []
for i in range(n):
    # 이름은 string형으로, 성적은 int형으로 변환하여 (이름, 성적) 형식으로 info에 추가
    student = (lambda x:(x[0],int(x[1])))(input().split())
    info.append(student)

# 성적순으로 info 정렬
info = sorted(info, key=lambda x:x[1])
# 성적이 낮은 순으로 이름 출력
for i in info:
    print(i[0], end=' ')