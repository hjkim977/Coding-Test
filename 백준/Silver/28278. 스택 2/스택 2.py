import sys
input=sys.stdin.readline
n=int(input())
stack=[]

for i in range(n):
    num=list(map(int,input().split()))

    if num[0]==1: #1번 명령
        stack.append(num[1])
    elif num[0]==2: #2번 명령
        if stack:
            p = stack.pop()
            print(p)
        else:
            print(-1)
    elif num[0]==3: #3번 명령
        print(len(stack))
    elif num[0]==4: #4번 명령
        if stack:
            print(0)
        else:
            print(1)
    else: #5번 명령
        if stack:
            print(stack[-1])
        else:
            print(-1)