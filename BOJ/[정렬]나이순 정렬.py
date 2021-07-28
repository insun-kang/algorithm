import sys

n = int(input())

lst = [(i, list(map(str, sys.stdin.readline().split()))) for i in range(n)]
lst = sorted(lst, key=lambda x: (int(x[1][0]), x[0]))
for i, j in lst:
    print(*j)
