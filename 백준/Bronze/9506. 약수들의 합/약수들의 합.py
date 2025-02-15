while 1:
    n=int(input())
    lis=[]

    if n==-1:
        break
    for i in range(1,n):
        if n%i==0:
            lis.append(i)
    if sum(lis)==n:
        print(n,"="," + ".join(map(str,lis)))
    else:
        print(n,"is NOT perfect.")