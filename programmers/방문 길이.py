def func(dirs, pos):
    x, y= pos
    road=[]
    cnt=0
    for i in dirs:
        if i == 'U':
            if 0<=y+1<11:
                temp=[[x, y],[x,y+1]]
                temp.sort()
                if temp not in road:
                    road.append(temp)
                    cnt+=1
                    y+=1  
                else:
                    y+=1
            else:
                 continue
        elif i== 'D':
            if 0<=y-1<11:
                temp=[[x, y],[x,y-1]]
                temp.sort()
                if temp not in road:
                    road.append(temp)
                    cnt+=1
                    y-=1  
                else:
                    y-=1
            else:
                 continue
        elif i == 'L':
            if 0<=x-1<11:
                temp=[[x, y],[x-1,y]]
                temp.sort()
                if temp not in road:
                    road.append(temp)
                    cnt+=1
                    x-=1  
                else:
                    x-=1
            else:
                 continue
        elif i == 'R':
            if 0<=x+1<11:
                temp=[[x, y],[x+1,y]]
                temp.sort()
                if temp not in road:
                    road.append(temp)
                    cnt+=1
                    x+=1  
                else:
                    x+=1
            else:
                 continue
    return cnt
def solution(dirs):  
    return func(dirs, [5,5])