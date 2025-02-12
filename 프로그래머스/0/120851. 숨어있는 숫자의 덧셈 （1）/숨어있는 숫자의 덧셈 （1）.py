def solution(my_string):
    total=0
    for i in my_string:
        if i.isdigit():
            total+=int(i)
    return total