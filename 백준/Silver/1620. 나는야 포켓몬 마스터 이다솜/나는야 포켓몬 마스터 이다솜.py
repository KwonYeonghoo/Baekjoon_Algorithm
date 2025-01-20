import sys

# {포켓몬이름: 숫자, 숫자: 포켓몬이름} 이렇게 저장?
N, M = map(int, input().split())
pokemon_dict = {}
for i in range(1, N + 1):
    pokemon_name = sys.stdin.readline().strip()
    pokemon_dict[pokemon_name] = i
    pokemon_dict[str(i)] = pokemon_name

for _ in range(M):
    question = sys.stdin.readline().strip()
    print(pokemon_dict[question])