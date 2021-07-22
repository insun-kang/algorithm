from collections import Counter
import sys

n = int(input())

lst = [int(sys.stdin.readline()) for _ in range(n)]
lst.sort()

avg = round(sum(lst)/len(lst))
med = lst[(len(lst)-1)//2]
mode = Counter(lst).most_common(2)
rang = max(lst) - min(lst)

if n !=1:
    if mode[0][1] == mode[1][1]:
        mode = mode[1][0]
    else:
        mode = mode[0][0]
else:
    mode = mode[0][0]

print(avg, med, mode, rang, sep = '\n')