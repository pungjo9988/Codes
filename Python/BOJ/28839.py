num = int(input())
if num % 5 == 0:
    print(num // 5)
elif num % 5 == 3:
    print(num // 5 + 1)
else:
    cnt_list = []
    for i in range(num // 5 + 1):
        if i == 0:
            if num % 3 == 0:
                cnt_list.append(num // 3)
        elif (num - (5 * i)) % 3 == 0:
            cnt_list.append(i + (num - (5 * i)) // 3)
    if len(cnt_list) == 0:
        print('-1')
    else:
        print(min(cnt_list))