T = int(input())
A = [i for i in range(1, 13)]
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):
        subset = []
        sum_v = 0
        for j in range(12):
            if i & (1 << j):
                subset.append(A[j])
                sum_v += A[j]

        if len(subset) == n and sum_v == k:
            cnt += 1
    print(f'#{test_case} {cnt}')
