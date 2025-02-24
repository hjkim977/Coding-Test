def solution(num_list):
    total=sum(num_list)**2
    mul=1
    for i in num_list:
        mul*=i
    if mul<total:
        return 1
    else:
        return 0
    