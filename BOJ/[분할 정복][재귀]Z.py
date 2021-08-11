def Z(n, r, c):
    global cnt
    if n == 1:
        if r == 0 and c == 0:
            pass
        elif r == 0 and c == 1:
            cnt += 1
        elif r == 1 and c == 0:
            cnt += 2
        else:
            cnt += 3
    else:
        if 0 <= r < 2**(n-1) and 0 <= c < 2**(n-1):  # 1
            return Z(n-1, r, c)
        elif 0 <= r < 2**(n-1) and 2**(n-1) <= c < 2**n:  # 2
            cnt += 2**(2*(n-1))
            return Z(n-1, r, c-(2**(n-2)))
        elif 2**(n-1) <= r < 2**n and 0 <= c < 2**(n-1):  # 3
            cnt += 2 * 2**(2*(n-1))
            return Z(n-1, r-(2**(n-2)), c)
        else:  # 4
            cnt += 3 * 2**(2*(n-1))
            return Z(n-1, r-(2**(n-2)), c-(2**(n-2)))


N, r, c = map(int, input().split())

cnt = 0

Z(N, r, c)

print(cnt)
