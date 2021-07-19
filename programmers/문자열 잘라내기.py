r, c = map(int, input().split())

alps=[input() for _ in range(r)]

count=0

while True:
    strings=[]
    check=0
    if count == c:
        break
    for i in range(c):
        tmp=''
        for j in range(count, r):
            tmp+=alps[j][i]
        if tmp not in strings:
            strings.append(tmp)
        else: 
            check=1   
            break
    if check == 1:
        break
    count+=1

       
print(count-1)