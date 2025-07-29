import sys
input=sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    a = []

    for _ in range(n):
        s = tuple(map(int,input().split()))
        a.append(s)
    a.sort()

    best = a[0][1]
    cnt = 1 #best 한명 뽑힘

    for i in range(1,len(a)):
        if best>a[i][1]:
            cnt+=1
            best = a[i][1]

    print(cnt)