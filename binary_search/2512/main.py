from sys import stdin

N = int(stdin.readline())
money = list(map(int, stdin.readline().split()))
budget = int(stdin.readline())

if sum(money) <= budget:
    print(max(money))
else:
    # 이진탐색
    money.sort()  # 오름차순 정렬
    start, end = 1, money[-1]  # 예산의 최소, 최댓값
    while start <= end:
        mid = (start + end) // 2  # 예산 제한
        cost = 0  # 비용
        for i in money:
            if i > mid:  # 예산보다 더 많으면 잘림
                cost += mid
            else:
                cost += i

        # 총 예산보다 크면, 최대 예산액을 줄임
        if cost > budget:
            end = mid - 1

        # 총 예산이 남으면, 최대 예산액을 늘림
        else:
            start = mid + 1
    print(end)