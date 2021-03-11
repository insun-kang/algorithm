from collections import deque

def convertTo1(num):
    q=deque()
    cnt=0
    q.append((num, cnt))
    while True:
        num, cnt =q.popleft()
        
        q.append((num-1, cnt+1))
        if num%3==0:
            num=num//3
            cnt+=1
            q.append((num, cnt))
        elif num%2==0:
            num=num//2
            cnt+=1
            q.append((num, cnt))
        else:
            num-=1
            cnt+=1
            q.append((num,cnt))
        if num==1:
            break
    return (q[-1][1])

def main():
    print(convertTo1(10))

if __name__ == "__main__":
    main()
