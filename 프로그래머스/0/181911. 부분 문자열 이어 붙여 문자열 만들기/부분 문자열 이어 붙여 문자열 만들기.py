def solution(my_strings, parts):
    word=''
    for i in range(len(my_strings)):
        string=my_strings[i]
        part=parts[i]
        for p in range(part[0],part[1]+1):
            word+=string[p]
    return word