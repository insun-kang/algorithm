n=int(input())

num=[]
result=[]
for i in range(n):
    n2=int(input())
    if n2==0:
        num.pop()
    else:
        num.append(n2)


print(sum(num))
