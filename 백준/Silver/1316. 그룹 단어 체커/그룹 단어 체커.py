n=int(input())
group_count=0
for a in range(n):
    w=input()
    group_list=[]
    is_group=True
    for i in range(len(w)):
        if w[i] not in group_list:
            group_list.append(w[i])
        else:
            if w[i]!=w[i-1]:
                is_group=False
                break
    if is_group==True:
        group_count+=1
print(group_count)