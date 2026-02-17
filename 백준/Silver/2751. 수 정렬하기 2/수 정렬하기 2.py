import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    i=int(input())
    arr.append(i)

arr.sort()
for i in arr:
    print(i)