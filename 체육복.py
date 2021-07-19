def solution(n, lost, reserve):
    answer = 0
    visited=[1]*n
    for i in lost:
        visited[i-1]=0
        
    reserve.sort()
    for i in reserve:
        if i in lost:
            visited[i-1]=1
            reserve.remove(i)
    
    
    for i in reserve:
        if visited[i-1]==0:
            visited[i-1]=1
        else:
            if i==1 and visited[i]==0:
                visited[i]=1
            elif i==n and visited[i-2]==0:
                visited[i-2]=1    
            elif i!=1 and i!=n and visited[i-2]==0 and visited[i]==0:
                visited[i-2]=1
            elif i!=1 and i!=n and visited[i-2]==0 and visited[i]==1:
                visited[i-2]=1
            elif i!=1 and i!=n and visited[i-2]==1 and visited[i]==0:
                visited[i]=1
            elif i!=1 and i!=n and visited[i-2]==1 and visited[i]==1:
                continue
            
            else:
                continue
    
    
    return sum(visited)