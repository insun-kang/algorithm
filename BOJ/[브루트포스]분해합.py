n = int(input())

for i in range(n):
    answer = i
    for j in str(i):
        answer += int(j)
    if answer == n:
        print(i)
        break
else:
    print(0)