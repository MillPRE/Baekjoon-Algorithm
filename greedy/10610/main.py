# 30의 배수가 되는 가장 큰 수 출력
# 없으면 -1 출력

N = list(input())
N.sort(reverse=True)
N = int("".join(N))
print(N if N % 30 == 0 else -1)
