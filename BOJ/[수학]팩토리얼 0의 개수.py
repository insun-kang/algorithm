def check(n):
    two = 0
    five = 0

    n_two = n
    n_five = n
    while True:
        if n_two % 2 != 0:
            result[0] += two
            break
        n_two = n_two//2
        two += 1
    while True:
        if n_five % 5 != 0:
            result[1] += five
            break
        n_five = n_five//5
        five += 1


N = int(input())
result = [0, 0]

for i in range(1, N+1):
    check(i)

print(min(result))
