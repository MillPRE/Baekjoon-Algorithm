from sys import stdin

N = int(stdin.readline())
kmList = list(map(int, stdin.readline().split()))
oilList = list(map(int, stdin.readline().split()))
pay = 0
curIdx = 0

while True:
    # print(curIdx)
    if curIdx >= len(oilList)-1:
        break

    # 현재 주유소에서 나보다 주유소 가격이 싼경우 전까지 다 사야함
    nextIdx = curIdx + 1
    for idx in range(curIdx +1, len(oilList)):
        if idx == len(oilList) - 1:
            nextIdx = idx
        if oilList[idx] < oilList[curIdx]:
            nextIdx = idx
            break
    # print("nextId", nextIdx)

    # 구매한 km oil 계산
    for idx in range(curIdx, nextIdx):
        pay += oilList[curIdx] * kmList[idx]

    curIdx = nextIdx
    # print("pay", pay)
    # print()
print(pay)