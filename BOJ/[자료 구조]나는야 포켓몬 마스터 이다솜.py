import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poketmons = {}
poketmons_name = {}

for i in range(1, N+1):
    t = input().rstrip()
    poketmons[i] = t
    poketmons_name[t] = i

for i in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(poketmons[int(question)])
    else:
        print(poketmons_name[question])
