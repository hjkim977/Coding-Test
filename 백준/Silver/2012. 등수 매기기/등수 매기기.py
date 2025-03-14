import sys
n=int(sys.stdin.readline())
real = [i for i in range(1,n+1)]
predict=[]

for _ in range(n):
    p=int(sys.stdin.readline())
    predict.append(p)
predict.sort()

total=0
for i in range(n):
    total+=abs(real[i]-predict[i])
print(total)