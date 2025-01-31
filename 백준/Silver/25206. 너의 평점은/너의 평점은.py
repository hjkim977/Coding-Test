h_sum=0
a_sum=0

level= {
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0,
}

for n in range(20):
    i=input().split()
    if i[2]=="P":
        continue
    class_avg=level[i[2]]
    a=float(i[1])*class_avg
    a_sum+=a
    h_sum+=float(i[1])
    main_avg=a_sum / h_sum
print(round(main_avg,7))