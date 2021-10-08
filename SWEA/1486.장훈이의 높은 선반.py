def recursion(start, s):
    global MIN
    if s >= B and MIN > s:
        MIN = s
        return
    if start == N:
        return
    recursion(start+1, s)
    recursion(start+1, s+talls[start])


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    talls = list(map(int, input().split()))
    MIN = int(1e9)
    recursion(0, 0)
    print(f'#{tc} {MIN-B}')
