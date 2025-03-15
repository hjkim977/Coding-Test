def solution(strArr):
    a=[]
    for i in strArr:
        if "ad" in i:
            a.append(i)
    for i in a:
        strArr.remove(i)
    return strArr