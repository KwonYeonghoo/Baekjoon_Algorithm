# 개선된 버전
# set 활용? --> set는 평균적으로 삽입/탐색에 O(1)의 시간 복잡도를 가지므로, 각 단어의 중복 제거를 보다 효율적으로 처리할 수 있다.
N = int(input())
count_dict = {i: set() for i in range(51)}  # 중복 방지를 위해 set 사용

for _ in range(N): # O(N)
    word = input()
    count_dict[len(word)].add(word) # 중복 제거를 바로 처리
    
for length in count_dict.keys(): # N번 다 돌지 않고 count_dict의 길이만큼 돈다 --> O(K logN)
    for value in sorted(count_dict[length]): # 정렬을 위 쪽 반복문이 아니라 여기서 진행
        print(value)