T = int(input())
for _ in range(T):
    N = int(input())
    closet = {}
    count = 1
    for _ in range(N):
        cloth, category = input().split()
        if category not in closet.keys():
            closet[category] = []
        closet[category] += [cloth]
    for key in closet.keys():
        count *= (len(closet[key]) + 1) # 의상을 착용하지 않은 상태도 하나의 의상이라 생각하고 1을 더해준다
    # 그럼 count는 가능한 모든 조합이 되고, 알몸인 경우의 수 -1만 해주고 출력
    print(count-1)