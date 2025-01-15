score_dict = {
    0:13,
    1:7,
    2:5,
    3:3,
    4:3,
    5:2
}
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_score = 0
for i in range(len(a)):
    a_score += score_dict[i] * a[i]

b_score = 1.5
for i in range(len(b)):
    b_score += score_dict[i] * b[i]

if a_score >= b_score:
    print("cocjr0208")
else: print("ekwoo")