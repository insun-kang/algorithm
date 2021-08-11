def binarySearch(a, key):
    start = 0
    end = len(a) - 1

    while start <= end:
        middle = (start + end)//2

        if a[middle] == key:
            return True
        elif a[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
    return False
