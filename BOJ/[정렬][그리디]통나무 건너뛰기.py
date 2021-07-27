t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    l.sort()

    answer=0

    for j in range(n-2):
        if l[j+2]-l[j]>answer:
            answer = l[j+2]-l[j]
    print(answer)

