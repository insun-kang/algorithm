
def is_vaild(end):
    for i in range(end):
        if lst[end] == lst[i] or abs(lst[end]-lst[i]) == abs(end-i):
            return False
    return True


def dfs(check):
    global cnt

    if check == n:
        cnt += 1
    else:
        for i in range(n):
            lst[check] = i
            if is_vaild(check):
                dfs(check+1)


n = int(input())
lst = [0 for _ in range(n)]
cnt = 0

dfs(0)
print(cnt)
