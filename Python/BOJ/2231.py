num = int(input())
a = True
for i in range(num):
    temp = list(str(i))
    sum = 0
    for j in temp:
        sum += int(j)
    if i + sum == num:
        print(i)
        a = False
        break
if a:
    print("0")