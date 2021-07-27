import sys

n = int(input())

pos = []

for _ in range(n):
    pos.append(list(map(int, sys.stdin.readline().split())))

pos = sorted(pos, key=lambda x: (x[0], x[1]))

for i in pos:
    print(*i)
