def power(num):
    if num == 1:
        return A % C
    else:
        temp = power(num //2)
        if num % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * A % C

A, B, C = map(int, input().split())
result = power(B)
print(result)