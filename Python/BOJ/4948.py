Max_num = 123456 * 2 + 1
num_arr = [True] * Max_num
for i in range(2, int(Max_num ** 0.5) + 1):
    if num_arr[i]:
        for j in range(2 * i, Max_num, i):
            num_arr[j] = False 
while True:
    num = int(input())
    if num == 0:
        break
    cnt = 0
    for i in range(num + 1, num * 2 + 1):
        if num_arr[i]:
            cnt += 1
    print(cnt)