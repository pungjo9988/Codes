n, m = map(int, input().split())
num_arr = list(map(int, input().split()))
num_arr = sorted(num_arr)
num_arr.reverse()
sum_arr = []
finish = False
for i in range(n - 2):
    if finish:
        break
    for j in range(i + 1, n - 1):
        if finish:
            break
        for k in range(j + 1, n):
            temp = num_arr[i] + num_arr[j] + num_arr[k]
            if temp < m:
                sum_arr.append(temp)
            elif temp == m:
                print(temp)
                finish = True
                break
if finish == False:
    print(max(sum_arr))