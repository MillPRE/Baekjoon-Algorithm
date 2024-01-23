from sys import stdin

# N 주어질 리스트 길이
# S 태수 점수
# P 랭킹 순위 수

N, S, P = map(int, stdin.readline().split())
scores = []

# 점수 리스트 세팅
if N > 0:
    scores = list(map(int, stdin.readline().split()))

scores.append(S)
scores.sort(reverse=True)

ranks = []
for idx in range(len(scores)):
    if idx == 0:
        ranks.append(1)
    elif idx != 0 and scores[idx-1] == scores[idx]:
        ranks.append(ranks[-1])
    else:
        ranks.append(len(ranks) + 1)

rank = -1
if len(ranks) <= P:
    index = scores.index(S)
    rank = ranks[index]
else:
    index = scores.index(S)
    rank = ranks[index]

    # 등수가 P와 같을 때 동점자 있는지 확인
    if rank == P and ranks.count(rank) > 1:
        rank = -1

    if rank < P < ranks.count(rank) + len(ranks[:index]):
        rank = -1

    # rank 가 P보다 큰 경우
    if rank > P:
        rank = -1

# print(ranks)
print(rank)