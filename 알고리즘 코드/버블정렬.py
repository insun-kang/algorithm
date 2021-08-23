def bubble(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print(lst)
    return lst


lst = [55, 78, 7, 12, 42]

print(bubble(lst))
