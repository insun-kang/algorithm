def change(x1, x2, y1, y2, table):
    tmp = []
    for i in range(x1, x2):
        tmp.append(table[y1][i])
    for i in range(y1, y2):
        tmp.append(table[i][x2])
    for i in range(x2, x1, -1):
        tmp.append(table[y2][i])
    for i in range(y2, y1, -1):
        tmp.append(table[i][x1])
    res = min(tmp)
    tmp.insert(0, tmp.pop())
    for i in range(x1, x2):
        table[y1][i] = tmp.pop(0)
    for i in range(y1, y2):
        table[i][x2] = tmp.pop(0)
    for i in range(x2, x1, -1):
        table[y2][i] = tmp.pop(0)
    for i in range(y2, y1, -1):
        table[i][x1] = tmp.pop(0)
    return res

def solution(rows, columns, queries):
    answer =[]
    table = [[] for _ in range(rows)]
    for r in range(rows):
        for c in range(1, columns+1):
            table[r].append(c+r*columns)
    for query in queries:
        y1 = query[0]-1
        x1 = query[1]-1
        y2 = query[2]-1
        x2 = query[3]-1
        answer.append(change(x1, x2, y1, y2, table))
    
        
    return answer