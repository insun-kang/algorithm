import sys

n = int(input())

lst = [input() for i in range(n)]
lst = set(lst)  # 중복제거
lst = sorted(lst, key=lambda x: (len(x), x))  # 길이순정렬하고 사전순으로 정렬

for i in lst:
    print(i)
