def hanoi(n, one, two, three):
    if n == 1:
        print(one, three)
    else:
        hanoi(n-1, one, three, two)
        print(one, three)
        hanoi(n-1, two, one, three)

n = int(input())

print(2**n - 1)
hanoi(n, 1, 2, 3)