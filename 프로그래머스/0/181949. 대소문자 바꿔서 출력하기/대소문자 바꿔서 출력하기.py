str = input()
answer = ''
for s in str:
    if s.isupper():
        s=s.lower()
        answer+=s
    else:
        s=s.upper()
        answer+=s
print(answer)