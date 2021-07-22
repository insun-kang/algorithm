import sys

n = int(input())

lst = [int(sys.stdin.readline()) for _ in range(n)]

lst.sort()

print(*lst, sep='\n')