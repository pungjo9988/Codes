num = input().split()
num1 = list(num[0])
num2 = list(num[1])
num1.reverse()
num2.reverse()
for i in range(3):
    if num1[i] != num2[i]:
        if num1[i] > num2[i]:
            for i in range(3):
                print(num1[i], end="")
            break
        else:
            for i in range(3):
                print(num2[i], end="")
            break