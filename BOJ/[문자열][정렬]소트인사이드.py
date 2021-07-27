n = input()

lst = list(n)

lst.sort(reverse = True)
answer = ''
for i in lst:
    answer += i

print(answer)
