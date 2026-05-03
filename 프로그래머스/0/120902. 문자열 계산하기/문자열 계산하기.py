def solution(my_string):
    s=my_string.split(" ")
    answer=0
    op="+"
    for i in s:
        if i.isdigit():
            num=int(i)
            if op=="+":
                answer+=num
            else:
                answer-=num
        else:
            op=i
    return answer