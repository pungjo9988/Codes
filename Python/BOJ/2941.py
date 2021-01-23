a = list(input())
cnt = len(a)
for i in range(cnt):
    if a[i] == '=':
        if a[i - 1] == 'z' and a[i - 2] == 'd':
            cnt -= 2
        elif a[i - 1] == 'c' or a[i - 1] == 's'  or a[i - 1] == 'z':
            cnt -= 1
    elif a[i] == '-':
        if a[i - 1] == 'c' or a[i - 1] == 'd':
            cnt -= 1
    elif a[i] == 'j':
        if a[i - 1] == 'l' or a[i - 1] == 'n':
            cnt -= 1
print(cnt)