def bus(K, N, busstop):
    now = 0
    cnt = 1
    exit = 0

    while True:
        if now+K >= N:
            return cnt-1
        if now + K == 0:
            return 0
        if busstop[now+K] == 'S':
            now += K
            busstop[now] = cnt
            cnt += 1
        else:
            now -= 1


T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    busstop = [0] * N

    for i in station:
        busstop[i] = 'S'
    print(f'#{test_case} {bus(K, N, busstop)}')
