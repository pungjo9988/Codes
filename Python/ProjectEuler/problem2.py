sum = 2
arr = [1, 2]
cnt = 1
while arr[cnt] <= 4000000:
    arr.append(arr[cnt] + arr[cnt - 1])
    cnt += 1
    if arr[cnt] % 2 == 0:
        sum += arr[cnt]
print(sum)