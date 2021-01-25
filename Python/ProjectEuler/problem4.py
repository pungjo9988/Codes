num = []
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        temp = i * j
        arr = list(str(temp))
        if len(arr) == 6:
            if arr[5] == arr[0] and arr[4] == arr[1] and arr[3] == arr[2]:
                num.append(temp)
        if len(arr) == 5:
            if arr[4] == arr[0] and arr[3] == arr[1]:
                num.append(temp)
        if len(arr) == 4:
            if arr[3] == arr[0] and arr[2] == arr[1]:
                num.append(temp)
print(max(num))