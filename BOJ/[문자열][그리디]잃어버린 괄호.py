n = input().split('-')
for i in range(len(n)):
    n[i] = sum(map(int, n[i].split('+')))

answer = n[0]
for i in range(1, len(n)):
    answer -= n[i]
print(answer)
