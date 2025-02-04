n=int(input())
w=set()
for _ in range(n):
    a,b=map(int,input().split())
    for x in range(a,a+10):
        for y in range(b,b+10):
            w.add((x,y))
print(len(w))