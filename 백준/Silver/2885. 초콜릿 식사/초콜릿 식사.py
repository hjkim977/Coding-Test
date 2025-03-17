import sys

k=int(sys.stdin.readline())
size=1
while k>size:
    size*=2

count=0
copy=size
if k==copy:
    print(size, 0)
else:
    while k > 0:
        if k >= copy:
            k -= copy
        else:
            count += 1
            copy //= 2   
    print(size, count)