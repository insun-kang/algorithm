
n=int(input())

tri=[]
for i in range(n):
    tri.append(list(map(int, input().split())))


for i in range(n-1):
    for j in range(len(tri[i])+1):
        if j==0:
            tri[i+1][j]=tri[i][j]+tri[i+1][j]
        
        elif j==len(tri[i]):
            tri[i+1][-1]=tri[i][-1]+tri[i+1][-1]
            
        else:
            tri[i+1][j]=max(tri[i][j - 1] + tri[i + 1][j], tri[i][j] + tri[i + 1][j])
                
print(max(tri[-1]))
        