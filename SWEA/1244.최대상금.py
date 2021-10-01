def dfs(cnt, l):
    global answer
    if cnt == change:
        answer = max(answer, int(value))
        return
    for i in range(l):
        for j in range(i+1, l):
            card[i], card[j] = card[j], card[i]
            value = (''.join(card))
            if (value, cnt+1) not in visit:
                visit.append((value, cnt+1))
                dfs(cnt+1, l)
            card[i], card[j] = card[j], card[i]


T = int(input())

for tc in range(1, T+1):
    info, change = map(int, input().split())
    card = list(str(info))
    visit = []
    answer = 0
    cnt = 0

    dfs(cnt, len(card))
    print(f'#{tc} {answer}')
