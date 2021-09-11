def check(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] != lst[0][0]:
                return False
    return True


def divide(lst, N):
    global answer
    if check(lst):
        answer += lst[0][0]
        return

    else:
        answer += '('
        for r in range(0, N, N//2):
            for c in range(0, N, N//2):
                new_lst = []

                for i in range(r, r+N//2):
                    tmp = []
                    for j in range(c, c+N//2):
                        tmp.append(lst[i][j])
                    new_lst.append(tmp)

                divide(new_lst, N//2)
        answer += ')'


N = int(input())
answer = ''
lst = [list(input()) for i in range(N)]
divide(lst, N)
print(answer)
