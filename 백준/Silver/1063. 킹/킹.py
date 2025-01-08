a2n = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
n2a = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}

dy = [-1, 0, 1, 0]  # B, R, T, L
dx = [0, 1, 0, -1]
dir_dict = {"B": 0, "R": 1, "T": 2, "L": 3}


king, rock, N = input().split()
N = int(N)

convert_pos = lambda x: [a2n[x[0]], int(x[1]) - 1]
king = convert_pos(king)
rock = convert_pos(rock)


def OOB(nx, ny):
    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
        return True
    else:
        return False


def move(pos, orders):
    for order in orders:
        idx = dir_dict[order]
        nx = pos[0] + dx[idx]
        ny = pos[1] + dy[idx]
        if OOB(nx, ny):
            return None
        pos = [nx, ny]
    return pos


for _ in range(N):
    order = input()
    if (move(king, order) is not None) and (rock != move(king, order)):
        king = move(king, order)
    elif (move(king, order) == rock) and (move(rock, order) is not None):
        king = move(king, order)
        rock = move(rock, order)
    else:
        continue

king = f"{n2a[king[0]]}{king[1]+1}"
rock = f"{n2a[rock[0]]}{rock[1]+1}"
print(f"{king}\n{rock}")