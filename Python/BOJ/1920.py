import sys
a = int(sys.stdin.readline())
temp1 = set(sys.stdin.readline().split())
a = int(sys.stdin.readline())
temp2 = sys.stdin.readline().split()
for i in temp2:
    sys.stdout.write('1\n') if i in temp1 else sys.stdout.write('0\n')
