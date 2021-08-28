def check(lst):
    a = lst[0][0]
    for i in lst:
        for j in i:
            if a != j:
                return False
    return True


def divide(lst, n):
    if check(lst):
        answer[lst[0][0]] += 1
    else:
        for rs in range(0, n, n//3):
            for cs in range(0, n, n//3):
                new_lst = []
                for i in range(rs, rs+n//3):
                    tmp = []
                    for j in range(cs, cs+n//3):
                        tmp.append(lst[i][j])
                    new_lst.append(tmp)
                divide(new_lst, n//3)


N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
answer = {-1: 0, 0: 0, 1: 0}

divide(paper, N)
for i in answer.values():
    print(i)
