def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True   

m = int(input())
n = int(input())
arr = []
sum = 0
first = True
for i in range(m, n + 1):
    if isPrime(i):
        sum += i
        arr.append(i)
if arr:
    print(sum)
    print(min(arr))
else:
    print('-1')