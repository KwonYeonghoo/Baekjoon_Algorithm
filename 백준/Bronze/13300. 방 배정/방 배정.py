import math

N, K = list(map(int, input().split()))


sex_grade = [list(map(int, input().split())) for _ in range(N)]
students = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

room_count = 0

for sex, grade in sex_grade:
    if sex == 0:
        students[grade-1][0] += 1
    else:
        students[grade-1][1] += 1

for student in students:
    room_count += math.ceil(student[0] / K)
    room_count += math.ceil(student[1] / K)

print(room_count)