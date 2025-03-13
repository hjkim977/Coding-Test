from collections import Counter

word=input()
word=''.join(sorted(word))
count=Counter(word)

odd=0
odd_char=""
half=""

for key,value in count.items():
    if value%2==1:
        odd+=1
        odd_char+=key
    half+=key*(value//2)

if odd>=2:
    print("I'm Sorry Hansoo")
else:
    print(half+odd_char+half[::-1])