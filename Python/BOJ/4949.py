while True:
    a = input()
    if a == '.':
        break
    a = list(a)
    arr = []
    for i in a:
        if i == '(' or i == '[':
            arr.append(i)
        elif i == ')':
            if arr:
                if arr[-1] == '(':
                    arr.pop()
                else:
                    break
            else:
                arr.append(i)
                break
        elif i == ']':
            if arr:
                if arr[-1] == '[':
                    arr.pop()
                else:
                    break
            else:
                arr.append(i)
                break
    if len(arr) == 0:
        print('yes')
    else:
        print('no')