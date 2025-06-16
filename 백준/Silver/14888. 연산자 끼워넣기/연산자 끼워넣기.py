n = int(input())
a = list(map(int,input().split()))
p,m,mul,d = list(map(int,input().split()))

max_result = -float('inf')
min_result = float('inf')

def backtrack(start, total, p, m, mul,d):
    global max_result, min_result

    if start == n:
        max_result = max(total,max_result)
        min_result = min(total,min_result)
        return

    if p:
        backtrack(start+1, total+a[start],p-1,m,mul,d)
    if m:
        backtrack(start+1, total-a[start],p,m-1,mul,d)
    if mul:
        backtrack(start+1, total*a[start],p,m,mul-1,d)
    if d:
        if total<0 and a[start]>0:
            backtrack(start+1, -((-total)//a[start]),p,m,mul,d-1)
        else:
            backtrack(start+1, total//a[start],p,m,mul,d-1)

backtrack(1,a[0],p,m,mul,d)

print(max_result)
print(min_result)