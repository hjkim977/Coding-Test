def solution(num_list):
    a=len(num_list)-1
    b=a-1
    if num_list[a]>num_list[b]:
        num_list.append(num_list[a]-num_list[b])
    else:
        num_list.append(num_list[a]*2)
    return num_list