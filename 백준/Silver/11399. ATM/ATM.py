n=int(input())
times=list(map(int, input().split()))
times.sort()
time,total=0,0

for i in times:
    time+=i
    total+=time
print(total)