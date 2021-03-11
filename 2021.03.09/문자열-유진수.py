num=input()

result1=1
result2=1
result3=0


for i in range(1, len(num)):
    j=len(num)-i
    for k in range(i):
        result1=result1*int(num[k])
    for l in range(i, len(num)):
        result2=result2*int(num[l])
    if result1==result2:
        result3+=1
        break
    result1=1
    result2=1
if result3>0:
    print('YES')
else:
    print('NO')