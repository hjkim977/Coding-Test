n=input()
l=[i for i in n]
l.sort(reverse=True)
l=map(str,l)
print(''.join(l))