def check(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] != lst[0][0]:
                return False
    return True

def divide(lst, n):
    global answer
    if check(lst):
        answer[lst[0][0]] += 1
    else:
        for r in range(0, n, n//2):
            for c in range(0, n, n//2):
                new_lst = []
                for i in range(r, r+n//2):
                    tmp = []
                    for j in range(c, c+n//2):
                        tmp.append(lst[i][j])
                    new_lst.append(tmp)
                divide(new_lst, n//2)


N = int(input())
answer = {0 : 0, 1 : 0}
paper = [list(map(int, input().split())) for _ in range(N)]

divide(paper, N)
for i in answer.values():
    print(i)