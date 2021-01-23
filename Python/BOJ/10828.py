import sys
input =  sys.stdin.readline
stack = []
cnt = int(input())
for i in range(cnt):
    op = input().split()
    if op[0] == 'push':
        stack.append(op[1])
    elif op[0] == 'pop':
        print(stack.pop()) if stack else print('-1')            
    elif op[0] == 'size':
        print(len(stack))
    elif op[0] == 'empty':
        print('0') if stack else print('1')
    elif op[0] == 'top':
        print(stack[-1]) if stack else print('-1') 