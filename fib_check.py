a=int(input("enter no. : "))
b=0
c=1
d=[]
for i in range(a):
    d.append(b)
    t=b+c
    b=c
    c=t
    if a==b:
        print("the given number is fibonacci number.")
if a not in d:
    print("the given number is not a fibonacci number.")