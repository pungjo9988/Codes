import sys
num = int(sys.stdin.readline())
arr = [i for i in range(1, num + 1)]
while len(arr) != 1:
    if len(arr) % 2:
        temp = [arr[-1]]
        temp.extend(arr[1::2])
        arr = temp
    else:
        arr = arr[1::2]
print(arr[0])