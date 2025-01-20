import sys
# 메모리 제한 4 MB
# add x: S에 x를 추가한다 (x가 이미 있는 경우에는 연산 무시)
# remove x: S에서 x를 제거한다 (x가 없는 경우 연산 무시)
# check x: S에 x가 있으면 1을, 없으면 0을 출력
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다.
# all: S를 {1, 2, ..., 20}으로 바꾼다
# empty: S를 공집합으로 바꾼다

M = int(input())
S = set()


def check(x):
    if x in S:
        return 1
    else:
        return 0


def add(x):
    if check(x):
        return
    S.add(x)


def remove(x):
    if not check(x):
        return
    S.remove(x)


def toggle(x):
    if check(x):
        remove(x)
    else:
        add(x)


def all():
    global S
    S = set(i for i in range(1, 21))


def empty():
    global S
    S = set()


for _ in range(M):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == "add":
        add(int(cmd[1]))
    elif cmd[0] == "remove":
        remove(int(cmd[1]))
    elif cmd[0] == "check":
        if check(int(cmd[1])):
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        toggle(int(cmd[1]))
    elif cmd[0] == "all":
        all()
    elif cmd[0] == "empty":
        empty()