a, b, c, d, f = map(int, input().split())
a = pow(a, 2)
b = pow(b, 2)
c = pow(c, 2)
d = pow(d, 2)
f = pow(f, 2)
sum = a + b + c + d + f
print(sum % 10)