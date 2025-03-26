def solution(answers):
    n = len(answers)
    answer = []
    students = {1: "12345", 2: "21232425", 3: "3311224455"}
    
    for student in range(1, 4):
        s = students[student]
        if len(s) < n:
            s = s * (n // len(s) + n % len(s))
            students[student] = s
    
    correct = {1:0, 2:0, 3:0}
    for i in range(len(answers)):
        for student in students:
            if str(answers[i]) == students[student][i]:
                correct[student] = correct[student] + 1
    
    max_score = max(correct.values())
    print(max_score)
    for c in correct:
        if correct[c] == max_score:
            answer.append(c)
            
            
    return answer