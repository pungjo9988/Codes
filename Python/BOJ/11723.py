import sys
S = []
for i in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if len(command) == 1:
        if command[0] == 'all':
            S = []
            S = list(range(1, 21))
        else:
            S = []
    else:
        op, num = command[0], command[1]
        num = int(num)
        if op == 'add':
            if num not in S:
                S.append(num)
        elif op == 'remove':
            if num in S:
                S.remove(num)
        elif op == 'check':
            if num in S:
                print('1')
            else:
                print('0')
        elif op == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.append(num)