import sys

input = sys.stdin.readline
n = int(input())

shape = []

for _ in range(n):
    x, y = map(int, input().split())
    shape.append((x, y))

shape = sorted(shape, key = lambda x : (x[0]))

shape.append(shape[0])
print(shape)
