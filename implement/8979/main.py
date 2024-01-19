from sys import stdin

# N: 참여 나라 수
# K: 등수 구하고자 하는 나라

# arr[0] 국가 나타내는 숫자
# arr[1] 금
# arr[2] 은
# arr[3] 동

N, K = map(int, stdin.readline().split())
scores = []
target = []

for _ in range(N):
    newScore = (list(map(int, stdin.readline().split())))
    if newScore[0] == K:
        target = newScore
    else:
        scores.append(newScore)

scores.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
win = []
lose = []

for idx in range(1, 4):
    for s in scores:
        if idx >= 2:
            if s not in win and s not in lose and s[idx] > target[idx]:
                win.append(s)
            elif s not in win and s not in lose and s[idx] < target[idx]:
                lose.append(s)
        else:
            if s[idx] > target[idx]:
                win.append(s)
            elif s[idx] < target[idx]:
                lose.append(s)
    for w in win:
        if w in scores:
            scores.remove(w)
    if len(lose) > 0:
        for l in lose:
            if l in scores:
                scores.remove(l)

print(len(win) +1)
