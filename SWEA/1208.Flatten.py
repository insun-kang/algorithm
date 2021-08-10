def func(dump, boxes):
    cnt = 0
    while True:
        max_h = 0
        min_h = 100
        storage = [0, 0]
        
        for i in range(len(boxes)):
            if boxes[i] >= max_h:
                max_h = boxes[i]
                storage[0] = i
            if boxes[i] <= min_h:
                min_h = boxes[i]
                storage[1] = i
        if cnt == dump:
            return max_h - min_h
        cnt +=1
        boxes[storage[0]] -= 1
        boxes[storage[1]] += 1
        
for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    
    print(f'#{test_case} {func(dump, boxes)}')
