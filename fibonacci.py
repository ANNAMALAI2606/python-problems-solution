a=int(input("enter no. : "))
b=0
c=1
d=[]
for i in range(a):
    d.append(b)
    b,c=c,b+c
'''   t=b+c
    b=c
    c=t'''

print("fibonacci series is ",d)