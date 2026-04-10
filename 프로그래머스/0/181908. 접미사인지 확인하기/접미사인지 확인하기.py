def solution(my_string, is_suffix):
    l=len(is_suffix)
    answer=my_string[-l:]
    if answer==is_suffix:
        return 1
    else:
        return 0