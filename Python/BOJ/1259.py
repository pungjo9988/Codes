while True:
    s = list(map(int, input()))
    if len(s) == 1 and s[0] == 0:
        break
    if s == s[::-1]:
        print('yes')
    else:
        print('no')