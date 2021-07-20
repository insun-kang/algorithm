from collections import Counter
def delblock(m,n,lst_board):
    map_=[[False for _ in range(n)] for _ in range(m)]
    cnt=0
    for i in range(m-1):
        for j in range(n-1):
            if lst_board[i][j]==lst_board[i+1][j]==lst_board[i][j+1]==lst_board[i+1][j+1]!=' ':
                map_[i][j]=True
                map_[i+1][j]=True
                map_[i][j+1]=True
                map_[i+1][j+1]=True
                cnt+=1
    
    return (map_, cnt)

def down(map_, lst_board, m ,n):
    for i in range(m):
        for j in range(n):
            if map_[i][j]==True:
                if i>0:
                    for k in range(i):
                        lst_board[i-k][j]=lst_board[i-k-1][j]
                        lst_board[i-k-1][j]=' '
                        
                else:
                    lst_board[i][j]=' '
    return lst_board


def solution(m, n, board):
    answer = 0
    lst_board=[]
    temp=[]
    for i in board:
        for j in i:
            temp.append(j)
        lst_board.append(temp)
        temp=[]
        
    while True:
        map_, cnt=delblock(m, n, lst_board)
        lst_board=down(map_, lst_board, m, n)
        if cnt==0:
            break
    for i in range(m):
        for j in range(n):
            if lst_board[i][j]==' ':
                answer+=1
    
    return answer