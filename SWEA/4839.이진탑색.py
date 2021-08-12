def binary_search(p, page):
    start = 1
    end = p
    mid = end//2
    cnt = 0
    while(1):
        cnt += 1
        if mid == page:
            return cnt
        elif mid > page:
            end = mid
        elif mid < page:
            start = mid
        mid = (end+start)//2


t = int(input())
for tc in range(1, t+1):
    p, a, b = map(int, input().split())

    cnta = binary_search(p, a)
    cntb = binary_search(p, b)
    if cnta == cntb:
        print('#'+str(tc), 0)
    elif cnta > cntb:
        print('#'+str(tc), 'B')
    else:
        print('#'+str(tc), 'A')
