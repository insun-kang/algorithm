n = int(input())

three=0


while True:
    m = n-three*3
    if m<0:
        print('-1')
        break
    if m==0:
        print(three)
        break
    if m%5 ==0:
        print(three + m//5)
        break
    
    
    three+=1
