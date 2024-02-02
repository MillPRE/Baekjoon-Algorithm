from sys import stdin

N, K = map(int, stdin.readline().split())
tables = list(stdin.readline().strip())
# print(N, K)
# print(tables)

count = 0
for idx in range(len(tables)):
    if tables[idx] == "P":
        startIdx = idx - K if idx - K >= 0 else 0
        endIdx = idx + K if idx + K < len(tables) else len(tables)-1
        for i in range(startIdx, endIdx+1):
            if tables[i] == "H":
                count += 1
                tables[i] = "X"
                break

# print(tables)
print(count)