n = int(input())

num = [input() for _ in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        if len(num[i]) > len(num[j]):
            num[i], num[j] = num[j], num[i]
        
        elif len(num[i]) == len(num[j]):
            sum_i=0
            sum_j=0
            for k in range(len(num[i])):
                if num[i][k].isdigit():
                    sum_i += int(num[i][k])
                if num[j][k].isdigit():
                    sum_j += int(num[j][k])
            if sum_i > sum_j:
                num[i], num[j] = num[j], num[i]
                
            elif sum_i == sum_j:
                if num[i] > num[j]:
                    num[i], num[j] = num[j], num[i]
for i in num:
    print(i)