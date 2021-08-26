N, M = map(int, input().split())
a = set()
for i in range(N):
    a.add(input())
b = set()
for i in range(M):
    b.add(input())
answer = list(a & b)
answer.sort()

print(len(answer))
print(*answer, sep='\n')
