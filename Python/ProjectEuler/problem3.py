def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input())
i = 2
while True:
    if num % i == 0:
        temp = num // i
        if isPrime(temp):
            print(temp)
            break
    i += 1