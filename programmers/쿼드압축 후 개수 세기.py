def solution(arr):
    cnt = [0, 0]
    N = len(arr)

    def split(x, y, n):
        init = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:
                    n = n // 2
                    split(x, y, n)
                    split(x, y + n, n)
                    split(x + n, y, n)
                    split(x + n, y + n, n)
                    return None
        if init==0:
            cnt[0] += 1
        else:
            cnt[1] += 1

    split(0, 0, N)
    return cnt