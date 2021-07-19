def solution(phone_book):
    answer = True
    cnt=0
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)):
        if i<len(phone_book)-1 and phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
        
    #     for j in phone_book:
    #         if i != j and j.startswith(i):
    #             return False
    #         else:
    #             continue
    # return True