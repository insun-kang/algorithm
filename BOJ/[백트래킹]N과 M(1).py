from itertools import permutations

n, m = map(int, input().split())

lst = list(permutations(range(1, n+1), m))


for i in lst:
    print(*i)
