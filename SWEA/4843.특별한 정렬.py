T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n):
        tmp = lst[i]
        idx = i
        if i % 2 == 0:
            for j in range(i+1, n):
                if lst[j] > tmp:
                    tmp = lst[j]
                    idx = j
            lst[i], lst[idx] = lst[idx], lst[i]
        else:
            for j in range(i+1, n):
                if lst[j] < tmp:
                    tmp = lst[j]
                    idx = j
            lst[i], lst[idx] = lst[idx], lst[i]

    print(f'#{test_case}', *lst[:10])
