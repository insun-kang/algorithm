N, M = map(int, input().split())

known = set(list(map(int, input().split()))[1:])

party = [list(map(int, input().split()))[1:] for _ in range(M)]
new = len(party)
old = 0

check = 0
while True:
    if old == new:
        break
    old = new

    for i in range(len(party)):
        for j in party[i]:
            if j in known:
                known.update(party[i])
                party.pop(i)
                check = 1
                break
        if check == 1:
            check = 0
            break
    new = len(party)

print(len(party))
