from math import ceil
F, M, K = map(int, input().split())
# F 여학생 수
# M 남학생 수
# K 인턴십 참가해야 하는 학생 수
team = 0

if F + M == K:
    print(team)
else:
    while True:
        if F >= 2 and M >= 1:
            team += 1
            F -= 2
            M -= 1
        elif F + M >= K:
            print(team)
            break
        elif F + M < K:
            K -= F + M
            team -= ceil(K / 3)
            print(team)
            break
