n, m = map(int, input().split())

def _get_2_or_five(n, t):
    cnt = 0
    while n > 0:
        cnt += n // t
        n //= t
    return cnt

cnt5 = _get_2_or_five(n, 5) - _get_2_or_five(n-m, 5) - _get_2_or_five(m, 5)
cnt2 = _get_2_or_five(n, 2) - _get_2_or_five(n-m, 2) - _get_2_or_five(m, 2)
print(min(cnt5, cnt2))