num = int(input())
my_num = num
cnt = 0
while(True):
    if num < 10:
        ten = 0
    else:
        ten = num // 10
    one = num % 10
    num = one * 10 + (one + ten) % 10
    cnt += 1
    if my_num == num:
        print(cnt)
        break