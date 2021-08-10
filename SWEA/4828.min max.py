def diff(lst):
    max_num = 0
    min_num = 1000000
    for i in lst:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    return max_num - min_num


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f"#{test_case} {diff(lst)}")
