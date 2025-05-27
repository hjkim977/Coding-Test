def solution(binomial):
    a,op,b=binomial.split()
    for i in op:
        if i=='+':
            return int(a)+int(b)
        elif i=='-':
            return int(a)-int(b)
        elif i=='*':
            return int(a)*int(b)