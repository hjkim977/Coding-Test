n=input()
total=0

if "0" not in n:
    print(-1)
else:
    for i in n:
        total+=int(i)
    
    if total%3!=0:
        print(-1)
    else:
        sort_num=sorted(n, reverse=True)
        sort_num="".join(sort_num)
        print(sort_num)