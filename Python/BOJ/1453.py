num = int(input())
a = []
a = map(int, input().split())
a = set(a)
a = list(a)
print(num - len(a))