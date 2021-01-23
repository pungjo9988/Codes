def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)

k, n = map(int, input().split())
answer = fact(k) // fact(n) // fact(k - n)
print(answer)