def solution(myString, pat):
    myString=myString.replace('A','C')
    myString=myString.replace('B','A')
    myString=myString.replace('C','B')
    if pat in myString:
        return 1
    return 0