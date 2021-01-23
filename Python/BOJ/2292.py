num = int(input())
room = 1
if num == 1:
    print(room)
else:
    cnt = 1
    plus = 6
    while True:
        room += 1
        cnt += plus
        if num <= cnt:
            print(room)
            break
        plus += 6