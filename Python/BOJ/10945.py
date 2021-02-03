import sys
arr = []
for i in range(int(sys.stdin.readline())):
    temp = sys.stdin.readline().split()
    if temp[0] == 'push':
        arr.append(int(temp[1]))
    elif temp[0] == 'pop':
        if len(arr) == 0:
            sys.stdout.write('-1')
            sys.stdout.write('\n')
        else:
            sys.stdout.write(str(arr[0]))
            sys.stdout.write('\n')
            del arr[0]
    elif temp[0] == 'size':
        sys.stdout.write(str(len(arr)))
        sys.stdout.write('\n')
    elif temp[0] == 'empty':
        if len(arr) == 0:
            sys.stdout.write('1')
            sys.stdout.write('\n')
        else:
            sys.stdout.write('0')
            sys.stdout.write('\n')
    elif temp[0] == 'front':
        if len(arr) == 0:
            sys.stdout.write('-1')
            sys.stdout.write('\n')
        else:
            sys.stdout.write(str(arr[0]))
            sys.stdout.write('\n')
    elif temp[0] == 'back':
        if len(arr) == 0:
            sys.stdout.write('-1')
            sys.stdout.write('\n')
        else:
            sys.stdout.write(str(arr[-1]))
            sys.stdout.write('\n')