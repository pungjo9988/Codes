arr = []
for i in range(int(input())):
    num = int(input())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)
sum = 0
for i in range(len(arr)):
    sum += arr[i]
print(sum)