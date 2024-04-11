# 30명의 학생
# 학생 명부에 1 ~ 30까지 번호
# 특별과제 28명 제출
# 제출 안 한 2명의 출석번호 구하는 프로그램

arr = [int(input()) for _ in range(28)]
student_no = [i for i in range(1,31)]

for num in arr:
    student_no[num-1] = 0

student_no = sorted(student_no, reverse=True)

print(student_no[1])
print(student_no[0])