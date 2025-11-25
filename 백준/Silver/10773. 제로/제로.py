import sys
input=sys.stdin.readline

k=int(input())
l=[]

for _ in range(k):
    num=int(input())
    if num==0:
        l.pop()
    else:
        l.append(num)
print(sum(l))