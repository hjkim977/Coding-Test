import sys
t=int(sys.stdin.readline())

for x in range(t):
    n=int(sys.stdin.readline())
    score=[]

    for y in range(n):
        d,i=list(map(int,sys.stdin.readline().split()))
        score.append((d,i))

    score.sort()
    best=score[0][1]

    count=1

    for d,i in score:
        if best>i:
            best=i
            count+=1
    print(count)