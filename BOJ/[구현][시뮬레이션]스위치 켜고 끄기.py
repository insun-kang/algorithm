def boy(idx):
    while idx <= n:
        if switch[idx] == 0:
            switch[idx] = 1
        else:
            switch[idx] = 0
        idx += idx
def girl(idx):
    check = min(idx-1, n - idx)
    left = idx-1
    right = idx + 1

    if switch[idx] == 0:
        switch[idx] = 1
    else:
        switch[idx] = 0

    while idx - check <= left and right <= idx + check:
        if switch[left] == switch[right]:
            if switch[left] == 0:
                switch[left] = 1
                switch[right] = 1
            else:
                switch[left] = 0
                switch[right] = 0
        else:
            break
        left -= 1
        right += 1
n = int(input())
switch = [-1] + list(map(int, input().split()))
m = int(input())
students = [list(map(int, input().split())) for _ in range(m)]


for student in students:
    if student[0] == 1:
        boy(student[1])
    else:
        girl(student[1])


for i in range(1, n+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
