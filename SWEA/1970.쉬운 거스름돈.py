T = int(input())

for tc in range(1, T+1):
    cost = int(input())
    money = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0
    }
    for key in money:
        while True:
            if cost-key >= 0:
                cost -= key
                money[key] += 1
            else:
                break
        if cost == 0:
            break
    answer = []
    for value in money.values():
        answer.append(value)
    print(f'#{tc}')
    print(*answer)
