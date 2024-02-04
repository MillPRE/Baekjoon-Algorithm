# 문제가 이해가 안되서
# https://corin-e.tistory.com/entry/%EB%B0%B1%EC%A4%80-2607-%EB%B9%84%EC%8A%B7%ED%95%9C-%EB%8B%A8%EC%96%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 참고

from sys import stdin

N = int(stdin.readline())
target = list(stdin.readline().strip())
result = 0

for _ in range(N-1):
    case = stdin.readline().strip()
    compare = target[:]
    cnt = 0
    for c in case:
        if c in compare:
            # 같은 글자 삭제
            compare.remove(c)
        else:
            # 다른 글자 있는 경우 갯수 + 1
            cnt += 1
    # ex) target AAB case BBA -> cnt = 1, compare = A
    if len(compare) < 2 and cnt < 2:
        result += 1

print(result)
