n=int(input())
for i in range(n):
    s=list(input())
    count=0

    for j in s:
        if j=="(":
            count+=1
        else:
            count-=1
        if count<0:
            print("NO")
            break
    else:
        if count==0:
            print("YES")
        else:
            print("NO")