s = input()
t = input()

while True:
    if len(s) >= len(t):
        break

    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]
if s == t:
    print(1)
else:
    print(0)
