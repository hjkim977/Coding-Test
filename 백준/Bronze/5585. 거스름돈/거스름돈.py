n=int(input())
money=1000
a=money-n

coin=[500,100,50,10,5,1]
count=0

for i in coin:
    count+=a//i
    a=a%i
print(count)