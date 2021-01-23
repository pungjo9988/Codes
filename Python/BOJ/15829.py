num = int(input())
alpa_arr = list(input())
sum = 0
for i in range(num):
    sum += (ord(alpa_arr[i]) - 96) * pow(31, i)
print(sum % 1234567891)