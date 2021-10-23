def bubble(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] >lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print(lst)
    return lst

def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] <lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx],lst[i]
        print(lst)
    return lst

def insertion_sort(lst):
    for i in range(1,len(lst)):
        for j in range(i,0,-1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
        print(lst)
    return lst

def merge_sort(lst):
    if len(lst) <=1:
        return lst
    mid = len(lst)//2
    low_lst = lst[:mid]
    high_lst = lst[mid:]

    merge_lst = []
    l = 0
    h = 0

    while l<len(low_lst) and h< len(high_lst):
        if high_lst[h] <low_lst[l]:
            merge_lst.append(high_lst[h])
            h+=1
        else:
            merge_lst.append(low_lst[l])
            l+=1
    merge_lst += low_lst[l:]
    merge_lst += high_lst[h:]

    return merge_lst

def quick_sort(lst):
    if len(lst) <=1:
        return lst
    pivot = len(lst)//2
    front_lst, pivot_lst, back_lst = [], [], []
    for value in lst:
        if value < lst[pivot]:
            front_lst.append(value)
        elif value > lst[pivot]:
            back_lst.append(value)
        else:
            pivot_lst.append(value)
    return quick_sort(front_lst) + quick_sort(pivot_lst) + quick_sort(back_lst)

lst = [55, 78, 7, 12, 42]

# print(bubble(lst))
# print(selection_sort(lst))
# print(insertion_sort(lst))
# print(merge_sort(lst))
print(quick_sort(lst))