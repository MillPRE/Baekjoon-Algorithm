K = []
W = []
for _ in range(10):
    W.append(int(input()))

for _ in range(10):
    K.append(int(input()))

K.sort(reverse=True)
W.sort(reverse=True)

kScore = K[0] + K[1] + K[2]
wScore = W[0] + W[1] + W[2]

print(wScore,kScore)