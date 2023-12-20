N = int(input())
scores = []
totalScores = []
for _ in range(N):
    scores.append(list(map(int, input().split())))

for i in range(N):
    runMax = max(scores[i][0], scores[i][1])
    trick = sorted(scores[i][2:], reverse=True)
    totalScores.append(runMax + trick[0] + trick[1])
print(max(totalScores))
