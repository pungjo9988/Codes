for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if x1 == x2 and y1 == y2 and r1 == r2:
        print("-1")
    elif r1 + r2 == a or max(r1, r2) - min(r1, r2) == a:
        print("1")
    elif  max(r1, r2) - min(r1, r2) < a and max(r1, r2) + min(r1, r2) > a:
        print("2")
    else:
        print("0")