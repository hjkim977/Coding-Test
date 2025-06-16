n,s = map(int,input().split())
l = list(map(int,input().split()))
cnt = 0

def backtrack(start,total):
    global cnt

    if start==n:
        if total==s:
            cnt+=1
        return

    backtrack(start+1, total+l[start])
    backtrack(start+1, total)

backtrack(0,0)

if s == 0:
    cnt -= 1
print(cnt)