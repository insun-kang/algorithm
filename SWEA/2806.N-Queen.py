def is_valid(end):
    for i in range(end):
        if lst[end] == lst[i] or abs(lst[end]-lst[i]) == abs(end-i):
            return False
    return True


def dfs(check):
    global cnt

    if check == N:
        cnt += 1
    else:
        for i in range(N):
            lst[check] = i
            if is_valid(check):
                dfs(check+1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [0]*(N)
    cnt = 0
    dfs(0)
    print(f'#{tc} {cnt}')
