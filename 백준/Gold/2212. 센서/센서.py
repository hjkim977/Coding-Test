import sys
n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
site=list(map(int,sys.stdin.readline().split()))

if k>=n: #런타임 에러 방지 
    print(0)
    sys.exit() #현재 실행 중인 프로그램을 즉시 종료

site.sort()
diff=[]

for i in range(1,n):
    diff.append(site[i]-site[i-1])

for i in range(1,k):
    diff.remove(max(diff))
print(sum(diff))