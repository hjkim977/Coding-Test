def solution(sizes):
    r=[] #가로
    c=[] #세로
    for w,h in sizes:
        if w>=h:
            r.append(w)
            c.append(h)
        else:
            r.append(h)
            c.append(w)
    return max(r)*max(c)