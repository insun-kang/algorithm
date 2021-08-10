def find_max(n, m, lst):
    max_sum = 0
    min_sum = 10000 * n
    for i in range(n-m+1):
        if max_sum < sum(lst[i:i+m]):
            max_sum = sum(lst[i:i+m])
        if min_sum > sum(lst[i:i+m]):
            min_sum = sum(lst[i:i+m])
    return max_sum - min_sum


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    print(f"#{test_case} {find_max(N, M, lst)}")
