n = int(input())

lst = list(map(int, input().split()))

lst2 = sorted(set(lst))

answer = {lst2[i]: i for i in range(len(lst2))}
for i in lst:
    print(answer[i], end=' ')


# 딕셔너리의 시간복잡도는 O(1)이다
