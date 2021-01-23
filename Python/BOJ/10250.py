for i in range(int(input())):
    arr = list(map(int, input().split()))
    num = arr[2] % arr[0]
    if num == 0:
        num = arr[0]
    print("%d" %num, end="")
    if num == arr[0]:
        num = arr[2] // arr[0]
    else:
        num = arr[2] // arr[0] + 1
    print("%02d" %num)